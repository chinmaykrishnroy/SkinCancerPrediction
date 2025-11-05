import sys, os
from interface import *
from ctypewinapi import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from connect import ConnectAPI, PredictAPI

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentWidget(self.ui.connectionStack)
        self.ui.textEdit.setReadOnly(True)
        self.ui.textEdit.setFocusPolicy(Qt.NoFocus)
        self.ui.textEdit.setContextMenuPolicy(Qt.NoContextMenu)
        self.ui.textEdit.setAcceptDrops(False)
        self.setWindowFlags(Qt.FramelessWindowHint)
        enable_window_shadow(self)
        self.show()
        self.edge_margin = 8
        self.resizing = False
        self.dragging = False
        self.resize_position = None
        self.drag_position = None
        self.current_cursor = None
        self.dark_theme = True
        self.ui.appCloseBtn.clicked.connect(self.close)
        self.ui.closeBtn.clicked.connect(self.close)
        self.ui.appMinBtn.clicked.connect(self.showMinimized)
        self.ui.themeBtn.clicked.connect(self.toggleTheme)
        self.ui.hostLineEdit.returnPressed.connect(self.on_host_enter)
        self.ui.portLineEdit.returnPressed.connect(self.on_port_enter)
        self.ui.connectBtn.clicked.connect(self.start_connection)
        self.ui.appResetBtn.clicked.connect(self.reset_to_connection)
        self.ui.imageBtn.imageSelected.connect(self.on_image_path)
        self.ui.imageBtn.clicked.connect(self.select_image)
        for sig in ("fileDropped", "imageDropped", "pathSelected", "fileSelected"):
            s = getattr(self.ui.imageBtn, sig, None)
            if callable(getattr(s, "connect", None)):
                s.connect(self.on_image_path)
        self.ui.resultBtn.clicked.connect(self.select_image)
        self.ui.hostLineEdit.setText("")
        self.ui.portLineEdit.setText("")
        self._connectThread = None
        self._predictThread = None
        self._base_url = None
        self._last_image = None

    def _clear_image_preview(self):
        try:
            self.ui.imageBtn._pix = None
            self.ui.imageBtn.setText("Image Here")
            self.ui.imageBtn.setIcon(QIcon())
        except Exception:
            pass

    def fail_back_to_connection(self, message=None):
        self._base_url = None
        self._last_image = None
        self.ui.connectionStack.setStyleSheet("background-color:#320000;")
        self.ui.hostLineEdit.clear()
        self.ui.portLineEdit.clear()
        self.ui.hostLineEdit.setPlaceholderText("FAILED")
        self.ui.portLineEdit.setPlaceholderText("FAILED")
        self.ui.connectBtn.setEnabled(True)
        self.ui.hostLineEdit.setEnabled(True)
        self.ui.portLineEdit.setEnabled(True)
        self._clear_image_preview()
        self.ui.textEdit.clear()
        self.ui.probablityLabel.setText("Confidence")
        self.ui.timeLabel.setText("Date Time")
        self.ui.stackedWidget.setCurrentWidget(self.ui.connectionStack)
        self.ui.hostLineEdit.setFocus()
        if message:
            self.set_log({"log": {"type": "error", "message": message}})

    def set_cursor(self, cursor):
        if self.current_cursor != cursor:
            self.setCursor(cursor)
            self.current_cursor = cursor

    def toggleTheme(self):
        if self.dark_theme:
            self.ui.themeBtn.setIcon(QIcon(':/icons/icons/cil-moon.png'))
            self.setStyleSheet(open("styles/light.css").read())
            self.dark_theme = False
        else:
            self.ui.themeBtn.setIcon(QIcon(':/icons/icons/cil-lightbulb.png'))
            self.setStyleSheet(open("styles/dark.css").read())
            self.dark_theme = True

    def mousePressEvent(self, event):
        rect = self.rect()
        x, y = event.pos().x(), event.pos().y()
        on_left = x <= self.edge_margin
        on_right = x >= rect.width() - self.edge_margin
        on_top = y <= self.edge_margin
        on_bottom = y >= rect.height() - self.edge_margin
        if on_left or on_right or on_top or on_bottom:
            self.resizing = True
            self.dragging = False
            self.resize_position = event.globalPos()
            if (on_right and on_bottom) or (on_left and on_top):
                self.set_cursor(Qt.SizeFDiagCursor)
            elif (on_left and on_bottom) or (on_right and on_top):
                self.set_cursor(Qt.SizeBDiagCursor)
            elif on_left or on_right:
                self.set_cursor(Qt.SizeHorCursor)
            else:
                self.set_cursor(Qt.SizeVerCursor)
        else:
            self.resizing = False
            self.dragging = True
            self.drag_position = event.globalPos() - self.pos()
            self.set_cursor(Qt.SizeAllCursor)

    def mouseMoveEvent(self, event):
        x, y = event.pos().x(), event.pos().y()
        rect = self.rect()
        if self.resizing:
            delta = event.globalPos() - self.resize_position
            self.resize(max(self.width() + delta.x(), 150), max(self.height() + delta.y(), 100))
            self.resize_position = event.globalPos()
            return
        if self.dragging:
            self.move(event.globalPos() - self.drag_position)
            return
        on_left = x <= self.edge_margin
        on_right = x >= rect.width() - self.edge_margin
        on_top = y <= self.edge_margin
        on_bottom = y >= rect.height() - self.edge_margin
        if (on_right and on_bottom) or (on_left and on_top):
            self.set_cursor(Qt.SizeFDiagCursor)
        elif (on_left and on_bottom) or (on_right and on_top):
            self.set_cursor(Qt.SizeBDiagCursor)
        elif on_left or on_right:
            self.set_cursor(Qt.SizeHorCursor)
        elif on_top or on_bottom:
            self.set_cursor(Qt.SizeVerCursor)
        else:
            self.set_cursor(Qt.ArrowCursor)

    def mouseReleaseEvent(self, event):
        self.resizing = False
        self.dragging = False
        self.set_cursor(Qt.ArrowCursor)

    def on_host_enter(self):
        self.ui.portLineEdit.setFocus()
        self.ui.portLineEdit.setCursorPosition(len(self.ui.portLineEdit.text()))

    def on_port_enter(self):
        self.start_connection()

    def start_connection(self):
        host = (self.ui.hostLineEdit.text() or "").strip()
        port = (self.ui.portLineEdit.text() or "").strip()
        self.clear_connection_error_state()
        if not host:
            self.ui.hostLineEdit.setPlaceholderText("HOST")
        if not port:
            self.ui.portLineEdit.setPlaceholderText("PORT")
        self.ui.connectBtn.setEnabled(False)
        self.ui.hostLineEdit.setEnabled(False)
        self.ui.portLineEdit.setEnabled(False)
        self._connectThread = ConnectAPI(host, port)
        self._connectThread.connectionResult.connect(self.on_connection_result)
        self._connectThread.start()

    def set_log(self, data):
        lg = (data.get("log") or {})
        msg = str(lg.get("message") or data.get("message") or "")
        typ = (lg.get("type") or "verbose").lower()
        col = "#ff4d4f" if typ == "error" else "#00c853" if typ == "success" else "#ffffff"
        self.ui.logLabel.setStyleSheet(f"color:{col};")
        self.ui.logLabel.setText(msg)

    def on_connection_result(self, success, data):
        self.ui.connectBtn.setEnabled(True)
        self.ui.hostLineEdit.setEnabled(True)
        self.ui.portLineEdit.setEnabled(True)
        self._base_url = data.get("_base_url")
        if success:
            self.ui.connectionStack.setStyleSheet("")
            self.apply_api_texts(data)
            self.set_log(data)
            self.ui.stackedWidget.setCurrentWidget(self.ui.mainStack)
        else:
            self.ui.hostLineEdit.clear()
            self.ui.portLineEdit.clear()
            self.ui.hostLineEdit.setPlaceholderText("FAILED")
            self.ui.portLineEdit.setPlaceholderText("FAILED")
            self.ui.connectionStack.setStyleSheet("background-color:#320000;")
            self.set_log(data)
            self.ui.stackedWidget.setCurrentWidget(self.ui.connectionStack)
            self.ui.hostLineEdit.setFocus()

    def apply_api_texts(self, data):
        t = data.get("ui_text", {}) or {}
        if t.get("resultBtn") is not None:
            self.ui.resultBtn.setText(str(t["resultBtn"]))
        if t.get("textEdit") is not None:
            self.ui.textEdit.setPlaceholderText(str(t["textEdit"]))
        if t.get("probablityLabel") is not None:
            self.ui.probablityLabel.setText(str(t["probablityLabel"]))
        if t.get("timeLabel") is not None:
            self.ui.timeLabel.setText(str(t["timeLabel"]))

    def clear_connection_error_state(self):
        self.ui.connectionStack.setStyleSheet("")
        if not self.ui.hostLineEdit.text():
            self.ui.hostLineEdit.setPlaceholderText("HOST")
        if not self.ui.portLineEdit.text():
            self.ui.portLineEdit.setPlaceholderText("PORT")

    def reset_to_connection(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.connectionStack)
        self.clear_connection_error_state()
        self.ui.hostLineEdit.clear()
        self.ui.portLineEdit.clear()
        self.ui.hostLineEdit.setFocus()
        self._base_url = None
        self._last_image = None
        self._clear_image_preview()
        self.ui.textEdit.clear()
        self.ui.probablityLabel.setText("Confidence")
        self.ui.timeLabel.setText("Date Time")

    def select_image(self):
        p, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Images (*.png *.jpg *.jpeg *.bmp *.webp);;All Files (*)")
        if p:
            self.on_image_path(p)

    def on_image_path(self, p):
        if isinstance(p, (list, tuple)):
            p = p[0] if p else ""
        if not p:
            return
        self.ui.imageBtn.setImage(p)
        self._last_image = p
        if not self._base_url:
            return
        self.start_predict(p)

    def start_predict(self, p):
        if not self._base_url:
            return
        self.ui.resultBtn.setEnabled(False)
        self._predictThread = PredictAPI(self._base_url, p)
        self._predictThread.predictResult.connect(self.on_predict_result)
        self._predictThread.start()

    def on_predict_result(self, success, data):
        self.ui.resultBtn.setEnabled(True)
        if success:
            self.apply_api_texts(data)
            self.ui.textEdit.setPlainText(str(data.get("description") or ""))
            self.ui.probablityLabel.setText(str(data.get("probability") or ""))
            self.ui.timeLabel.setText(str(data.get("time") or ""))
            self.set_log(data)
        else:
            self.set_log(data)
            msg = str((data.get("log") or {}).get("message") or data.get("message") or "")
            error_markers = ("Failed to establish a new connection", "Max retries exceeded", "Connection refused", "timed out")
            if any(m in msg for m in error_markers):
                self.fail_back_to_connection(msg)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
