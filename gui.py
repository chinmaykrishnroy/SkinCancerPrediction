import sys, numpy as np, tensorflow as tf
from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QLabel,QPushButton,QFileDialog,QTextEdit
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt,QThread,pyqtSignal
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D,MaxPooling2D,Flatten,Dense,Dropout

styles="""
QWidget {
    background-color: #121212;
    color: #E0E0E0;
    font-family: "Segoe UI", sans-serif;
    font-size: 14px;
}
QLabel {
    color: #FFFFFF;
    font-weight: bold;
    border: 2px solid #1E1E1E;
    border-radius: 10px;
    padding: 10px;
    background-color: #1E1E1E;
}
QPushButton {
    color: #FFFFFF;
    background-color: #1F1F1F;
    border: 2px solid #6200EE;
    border-radius: 8px;
    padding: 8px;
}
QPushButton:hover {
    background-color: #6200EE;
    color: #FFFFFF;
}
QPushButton:pressed {
    background-color: #3700B3;
}
QTextEdit {
    background-color: #1E1E1E;
    border: 2px solid #6200EE;
    border-radius: 10px;
    color: #E0E0E0;
    padding: 8px;
    font-family: "Consolas", monospace;
    font-size: 13px;
}
QScrollBar:vertical {
    background: #1E1E1E;
    width: 12px;
    margin: 0px 0px 0px 0px;
    border-radius: 6px;
}
QScrollBar::handle:vertical {
    background: #6200EE;
    min-height: 20px;
    border-radius: 6px;
}
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0px;
}
"""

MODEL_PATH="model/skin_cancer_cnn.h5"
SEVERITY={0.5:"Mild skin irregularity detected. Monitor closely.",
          0.6:"Moderate skin abnormality detected. Consider dermatologist consultation.",
          0.7:"Significant malignant features detected. Medical advice recommended.",
          0.8:"High-risk melanoma detected. Immediate professional assessment needed.",
          0.9:"Severe melanoma detected. Urgent medical intervention required.",
          0.95:"Critical melanoma detected. Immediate clinical attention required."}

def get_severity(prob):
    for t in sorted(SEVERITY.keys()):
        if prob<=t: return SEVERITY[t]
    return SEVERITY[sorted(SEVERITY.keys())[-1]]

class LoaderThread(QThread):
    finished=pyqtSignal(object)
    error=pyqtSignal(str)
    def run(self):
        try:
            m=Sequential([Conv2D(32,(3,3),activation='relu',input_shape=(224,224,3)),
                          MaxPooling2D((2,2)),Conv2D(64,(3,3),activation='relu'),
                          MaxPooling2D((2,2)),Conv2D(128,(3,3),activation='relu'),
                          MaxPooling2D((2,2)),Flatten(),Dense(512,activation='relu'),
                          Dropout(0.5),Dense(1,activation='sigmoid')])
            m.load_weights(MODEL_PATH)
            self.finished.emit(m)
        except Exception as e: self.error.emit(f"Error loading model:\n{e}")

class SkinCancerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Skin Cancer Detection")
        self.setGeometry(200,200,600,600)
        self.model=None
        self.setAcceptDrops(True)
        self.layout=QVBoxLayout();self.setLayout(self.layout)
        self.image_label=QLabel("Drag & drop an image here or click 'Select Image'")
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setFixedSize(400,400)
        self.layout.addWidget(self.image_label)
        self.select_button=QPushButton("Select Image")
        self.select_button.setEnabled(False)
        self.select_button.clicked.connect(self.open_file)
        self.layout.addWidget(self.select_button)
        self.result_text=QTextEdit()
        self.result_text.setReadOnly(True)
        self.result_text.setText("Loading model, please wait...")
        self.layout.addWidget(self.result_text)
        self.loader=LoaderThread()
        self.loader.finished.connect(self.model_loaded)
        self.loader.error.connect(self.model_error)
        self.loader.start()

    def model_loaded(self,m): self.model=m;self.result_text.setText("Model loaded! You can now select an image.");self.select_button.setEnabled(True)
    def model_error(self,msg): self.result_text.setText(msg)
    def dragEnterEvent(self,e): e.acceptProposedAction() if e.mimeData().hasUrls() else None
    def dropEvent(self,e): 
        if self.model and e.mimeData().urls(): self.process_image(e.mimeData().urls()[0].toLocalFile())
    def open_file(self):
        if self.model:
            f,_=QFileDialog.getOpenFileName(self,"Select Image","","Images (*.png *.jpg *.jpeg)")
            if f: self.process_image(f)
    def process_image(self,f):
        try:
            pixmap=QPixmap(f).scaled(self.image_label.width(),self.image_label.height(),Qt.KeepAspectRatio)
            self.image_label.setPixmap(pixmap)
            with open(f,"rb") as file: img_bytes=file.read()
            img=tf.io.decode_image(img_bytes,channels=3,expand_animations=False)
            img=tf.image.resize(tf.cast(img,tf.float32)/255.0,[224,224])
            x=tf.expand_dims(img,0).numpy()
            prob=float(self.model.predict(x)[0][0])
            if prob>0.5: label="Malignant";desc=get_severity(prob)
            else: label="Benign";desc="No immediate concern."
            self.result_text.setText(f"Prediction: {label}\nProbability: {prob:.2f}\n{desc}")
        except Exception as e: self.result_text.setText(f"Error processing image:\n{e}")

if __name__=="__main__":
    app=QApplication(sys.argv)
    app.setStyleSheet(styles)
    w=SkinCancerApp()
    w.show()
    sys.exit(app.exec_())
