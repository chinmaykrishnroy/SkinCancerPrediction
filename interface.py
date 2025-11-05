# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfacevxcEFu.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon, QMovie,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform,
                           QDesktopServices)
from PyQt5.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
                               QLabel, QLineEdit, QMainWindow, QPushButton,
                               QScrollArea, QSizePolicy, QSlider, QSpacerItem,
                               QStackedWidget, QToolButton, QVBoxLayout, QWidget, QTextEdit)

import res
from dropbutton import ImageDropButton

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(874, 588)
        MainWindow.setStyleSheet(open('styles/darker.css').read())
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_6 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.mainStack = QWidget()
        self.mainStack.setObjectName(u"mainStack")
        self.verticalLayout_3 = QVBoxLayout(self.mainStack)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.headerContainer = QWidget(self.mainStack)
        self.headerContainer.setObjectName(u"headerContainer")
        self.verticalLayout = QVBoxLayout(self.headerContainer)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QWidget(self.headerContainer)
        self.header.setObjectName(u"header")
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.header.sizePolicy().hasHeightForWidth())
        self.header.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QHBoxLayout(self.header)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.appIconTitleFrame = QFrame(self.header)
        self.appIconTitleFrame.setObjectName(u"appIconTitleFrame")
        self.appIconTitleFrame.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_4 = QHBoxLayout(self.appIconTitleFrame)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(4, 0, 6, 0)
        self.appIconBtn = QToolButton(self.appIconTitleFrame)
        self.appIconBtn.setObjectName(u"appIconBtn")
        self.appIconBtn.setMinimumSize(QSize(24, 24))
        icon = QIcon()
        icon.addFile(u":/icons/icons/feather.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.appIconBtn.setIcon(icon)
        self.appIconBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.appIconBtn)

        self.appTitleBtn = QPushButton(self.appIconTitleFrame)
        self.appTitleBtn.setObjectName(u"appTitleBtn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.appTitleBtn.sizePolicy().hasHeightForWidth())
        self.appTitleBtn.setSizePolicy(sizePolicy1)
        self.appTitleBtn.setMinimumSize(QSize(108, 0))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setBold(True)
        font.setWeight(75)
        self.appTitleBtn.setFont(font)

        self.horizontalLayout_4.addWidget(self.appTitleBtn)


        self.horizontalLayout_2.addWidget(self.appIconTitleFrame)

        self.netSpeedFrame = QFrame(self.header)
        self.netSpeedFrame.setObjectName(u"netSpeedFrame")
        self.netSpeedFrame.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_9 = QHBoxLayout(self.netSpeedFrame)
        self.horizontalLayout_9.setSpacing(9)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(9, 9, 9, 9)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer)


        self.horizontalLayout_2.addWidget(self.netSpeedFrame)

        self.appControlFrame = QFrame(self.header)
        self.appControlFrame.setObjectName(u"appControlFrame")
        self.horizontalLayout = QHBoxLayout(self.appControlFrame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.themeBtn = QToolButton(self.appControlFrame)
        self.themeBtn.setObjectName(u"themeBtn")
        self.themeBtn.setMinimumSize(QSize(28, 28))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/cil-lightbulb.png", QSize(), QIcon.Normal, QIcon.Off)
        self.themeBtn.setIcon(icon1)
        self.themeBtn.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.themeBtn)

        self.appMinBtn = QToolButton(self.appControlFrame)
        self.appMinBtn.setObjectName(u"appMinBtn")
        self.appMinBtn.setMinimumSize(QSize(28, 28))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.appMinBtn.setIcon(icon2)
        self.appMinBtn.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.appMinBtn)

        # REMOVED appMaxBtn

        self.appCloseBtn = QToolButton(self.appControlFrame)
        self.appCloseBtn.setObjectName(u"appCloseBtn")
        self.appCloseBtn.setMinimumSize(QSize(28, 28))
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.appCloseBtn.setIcon(icon4)
        self.appCloseBtn.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.appCloseBtn)


        self.horizontalLayout_2.addWidget(self.appControlFrame)


        self.verticalLayout.addWidget(self.header)


        self.verticalLayout_3.addWidget(self.headerContainer)

        self.predictionWidget = QWidget(self.mainStack)
        self.predictionWidget.setObjectName(u"predictionWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.predictionWidget.sizePolicy().hasHeightForWidth())
        self.predictionWidget.setSizePolicy(sizePolicy2)
        self.horizontalLayout_3 = QHBoxLayout(self.predictionWidget)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.imagePreviewWidget = QWidget(self.predictionWidget)
        self.imagePreviewWidget.setObjectName(u"imagePreviewWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.imagePreviewWidget.sizePolicy().hasHeightForWidth())
        self.imagePreviewWidget.setSizePolicy(sizePolicy3)
        self.verticalLayout_2 = QVBoxLayout(self.imagePreviewWidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.imageBtn = ImageDropButton(self.imagePreviewWidget)
        self.imageBtn.setObjectName(u"imageBtn")
        sizePolicy2.setHeightForWidth(self.imageBtn.sizePolicy().hasHeightForWidth())
        self.imageBtn.setSizePolicy(sizePolicy2)

        self.verticalLayout_2.addWidget(self.imageBtn)


        self.horizontalLayout_3.addWidget(self.imagePreviewWidget)

        self.outputWidget = QWidget(self.predictionWidget)
        self.outputWidget.setObjectName(u"outputWidget")
        self.verticalLayout_5 = QVBoxLayout(self.outputWidget)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.allInfoWidget = QWidget(self.outputWidget)
        self.allInfoWidget.setObjectName(u"allInfoWidget")
        self.allInfoWidget.setEnabled(True)
        self.verticalLayout_4 = QVBoxLayout(self.allInfoWidget)
        self.verticalLayout_4.setSpacing(4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(2, 0, 8, 0)
        self.resultBtn = QPushButton(self.allInfoWidget)
        self.resultBtn.setObjectName(u"resultBtn")

        self.verticalLayout_4.addWidget(self.resultBtn)

        self.textEdit = QTextEdit(self.allInfoWidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setEnabled(True)
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy4)

        self.verticalLayout_4.addWidget(self.textEdit)

        self.moreInfoWidget = QWidget(self.allInfoWidget)
        self.moreInfoWidget.setObjectName(u"moreInfoWidget")
        self.horizontalLayout_6 = QHBoxLayout(self.moreInfoWidget)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.probablityLabel = QLabel(self.moreInfoWidget)
        self.probablityLabel.setObjectName(u"probablityLabel")
        self.probablityLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.probablityLabel)

        self.timeLabel = QLabel(self.moreInfoWidget)
        self.timeLabel.setObjectName(u"timeLabel")
        self.timeLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.timeLabel)


        self.verticalLayout_4.addWidget(self.moreInfoWidget, 0, Qt.AlignTop)


        self.verticalLayout_5.addWidget(self.allInfoWidget, 0, Qt.AlignVCenter)


        self.horizontalLayout_3.addWidget(self.outputWidget)


        self.verticalLayout_3.addWidget(self.predictionWidget)

        self.footer = QWidget(self.mainStack)
        self.footer.setObjectName(u"footer")
        self.horizontalLayout_5 = QHBoxLayout(self.footer)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.logWidget = QWidget(self.footer)
        self.logWidget.setObjectName(u"logWidget")
        self.horizontalLayout_10 = QHBoxLayout(self.logWidget)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.logLabel = QLabel(self.logWidget)
        self.logLabel.setObjectName(u"logLabel")
        sizePolicy.setHeightForWidth(self.logLabel.sizePolicy().hasHeightForWidth())
        self.logLabel.setSizePolicy(sizePolicy)
        self.logLabel.setTextFormat(Qt.PlainText)
        self.logLabel.setScaledContents(False)
        self.logLabel.setAlignment(Qt.AlignCenter)
        self.logLabel.setWordWrap(False)

        self.horizontalLayout_10.addWidget(self.logLabel)


        self.horizontalLayout_5.addWidget(self.logWidget)

        self.footerRightBtnFrame = QFrame(self.footer)
        self.footerRightBtnFrame.setObjectName(u"footerRightBtnFrame")
        self.footerRightBtnFrame.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_8 = QHBoxLayout(self.footerRightBtnFrame)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 4, 0)
        self.appResetBtn = QPushButton(self.footerRightBtnFrame)
        self.appResetBtn.setObjectName(u"appResetBtn")
        self.appResetBtn.setMinimumSize(QSize(18, 18))
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/cil-reload.png", QSize(), QIcon.Normal, QIcon.Off)
        self.appResetBtn.setIcon(icon5)
        self.appResetBtn.setIconSize(QSize(14, 14))

        self.horizontalLayout_8.addWidget(self.appResetBtn)


        self.horizontalLayout_5.addWidget(self.footerRightBtnFrame)

        self.horizontalLayout_5.setStretch(0, 2)

        self.verticalLayout_3.addWidget(self.footer)

        self.stackedWidget.addWidget(self.mainStack)
        self.connectionStack = QWidget()
        self.connectionStack.setObjectName(u"connectionStack")
        self.verticalLayout_8 = QVBoxLayout(self.connectionStack)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.closeWidget = QWidget(self.connectionStack)
        self.closeWidget.setObjectName(u"closeWidget")
        self.horizontalLayout_7 = QHBoxLayout(self.closeWidget)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.closeBtn = QToolButton(self.closeWidget)
        self.closeBtn.setObjectName(u"closeBtn")
        self.closeBtn.setMinimumSize(QSize(28, 28))
        self.closeBtn.setMaximumSize(QSize(35, 35))
        self.closeBtn.setIcon(icon4)
        self.closeBtn.setIconSize(QSize(32, 32))

        self.horizontalLayout_7.addWidget(self.closeBtn)


        self.verticalLayout_8.addWidget(self.closeWidget, 0, Qt.AlignRight|Qt.AlignTop)

        self.connectionWidget = QWidget(self.connectionStack)
        self.connectionWidget.setObjectName(u"connectionWidget")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.connectionWidget.sizePolicy().hasHeightForWidth())
        self.connectionWidget.setSizePolicy(sizePolicy5)
        self.verticalLayout_9 = QVBoxLayout(self.connectionWidget)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.connectionFrame = QFrame(self.connectionWidget)
        self.connectionFrame.setObjectName(u"connectionFrame")
        sizePolicy5.setHeightForWidth(self.connectionFrame.sizePolicy().hasHeightForWidth())
        self.connectionFrame.setSizePolicy(sizePolicy5)
        self.verticalLayout_7 = QVBoxLayout(self.connectionFrame)
        self.verticalLayout_7.setSpacing(8)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.hostWidget = QWidget(self.connectionFrame)
        self.hostWidget.setObjectName(u"hostWidget")
        self.horizontalLayout_11 = QHBoxLayout(self.hostWidget)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, -1, 0)
        self.hostLineEdit = QLineEdit(self.hostWidget)
        self.hostLineEdit.setObjectName(u"hostLineEdit")
        self.hostLineEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.hostLineEdit)


        self.verticalLayout_7.addWidget(self.hostWidget)

        self.portWidget = QWidget(self.connectionFrame)
        self.portWidget.setObjectName(u"portWidget")
        self.verticalLayout_10 = QVBoxLayout(self.portWidget)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, -1, 0)
        self.portLineEdit = QLineEdit(self.portWidget)
        self.portLineEdit.setObjectName(u"portLineEdit")
        self.portLineEdit.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.portLineEdit)


        self.verticalLayout_7.addWidget(self.portWidget)


        self.verticalLayout_9.addWidget(self.connectionFrame, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_8.addWidget(self.connectionWidget)

        self.proceedWidget = QWidget(self.connectionStack)
        self.proceedWidget.setObjectName(u"proceedWidget")
        self.proceedWidget.setMinimumSize(QSize(0, 35))
        self.horizontalLayout_12 = QHBoxLayout(self.proceedWidget)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.connectBtn = QToolButton(self.proceedWidget)
        self.connectBtn.setObjectName(u"connectBtn")
        self.connectBtn.setMinimumSize(QSize(35, 35))
        self.connectBtn.setMaximumSize(QSize(35, 35))
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/cil-arrow-right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.connectBtn.setIcon(icon6)

        self.horizontalLayout_12.addWidget(self.connectBtn)


        self.verticalLayout_8.addWidget(self.proceedWidget, 0, Qt.AlignRight|Qt.AlignVCenter)

        self.stackedWidget.addWidget(self.connectionStack)

        self.verticalLayout_6.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
#if QT_CONFIG(shortcut)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Generic Web API Frontend", None))
        self.appIconBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.appTitleBtn.setText(QCoreApplication.translate("MainWindow", u"Skin Cancer Detector", None))
        self.themeBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.appMinBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        # REMOVED self.appMaxBtn line
        self.appCloseBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.imageBtn.setText(QCoreApplication.translate("MainWindow", u"Image Here", None))
        self.resultBtn.setText(QCoreApplication.translate("MainWindow", u"Title of the Result", None))
        self.textEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"The Description Goes Here for the Image Data Predicted by the Model!", None))
        self.probablityLabel.setText(QCoreApplication.translate("MainWindow", u"Confidence", None))
        self.timeLabel.setText(QCoreApplication.translate("MainWindow", u"Date Time", None))
        self.logLabel.setText(QCoreApplication.translate("MainWindow", u"Connected to API!", None))
        self.appResetBtn.setText("")
        self.closeBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.hostLineEdit.setText("")
        self.hostLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"HOST", None))
        self.portLineEdit.setText("")
        self.portLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"PORT", None))
        self.connectBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
    # retranslateUi
