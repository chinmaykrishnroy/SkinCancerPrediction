from PyQt5.QtWidgets import QPushButton, QSizePolicy
from PyQt5.QtGui import QPixmap, QIcon, QPainter, QPainterPath
from PyQt5.QtCore import Qt, QSize, pyqtSignal

class ImageDropButton(QPushButton):
    imageSelected = pyqtSignal(str)

    def __init__(self, parent=None, text="Drag & Drop Image"):
        super().__init__(text, parent)
        self._pix=None
        self.setAcceptDrops(True)
        self.setObjectName("imageBtn")
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setMaximumSize(650,650)

    def dragEnterEvent(self,e):
        u=e.mimeData().urls()
        f=u[0].toLocalFile().lower() if u else ""
        e.acceptProposedAction() if f.endswith((".png",".jpg",".jpeg",".bmp",".gif")) else e.ignore()

    def dropEvent(self,e):
        p=e.mimeData().urls()[0].toLocalFile()
        self.setImage(p)
        self.imageSelected.emit(p)

    def setImage(self,p): 
        px=QPixmap(p)
        if px.isNull(): return
        self._pix=px
        self.setText("")
        self.updateIcon()

    def resizeEvent(self,e): 
        super().resizeEvent(e)
        self.updateIcon()

    def updateIcon(self):
        if not self._pix: return
        s=min(self.width(),self.height(),400)
        img=self._pix.scaled(s,s,Qt.KeepAspectRatioByExpanding,Qt.SmoothTransformation)
        x,y=(img.width()-s)//2,(img.height()-s)//2
        img=img.copy(x,y,s,s)
        r=28
        m=QPixmap(s,s)
        m.fill(Qt.transparent)
        p=QPainter(m)
        p.setRenderHint(QPainter.Antialiasing)
        path=QPainterPath()
        path.addRoundedRect(0,0,s,s,r,r)
        p.setClipPath(path)
        p.drawPixmap(0,0,img)
        p.end()
        self.setIcon(QIcon(m))
        self.setIconSize(QSize(s,s))
