from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class DowloadWindow(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(500, 200)
        Form.setMinimumSize(QSize(500, 200))
        Form.setMaximumSize(QSize(500, 200))
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.background_frame_dowload = QFrame(Form)
        self.background_frame_dowload.setObjectName(u"background_frame_dowload")
        self.background_frame_dowload.setFrameShape(QFrame.StyledPanel)
        self.background_frame_dowload.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.background_frame_dowload)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.conten_dowload = QFrame(self.background_frame_dowload)
        self.conten_dowload.setObjectName(u"conten_dowload")
        self.conten_dowload.setFrameShape(QFrame.StyledPanel)
        self.conten_dowload.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.conten_dowload)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame = QFrame(self.conten_dowload)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(50, 50))
        self.label_2.setPixmap(QPixmap(u"./assets/icons/downloading.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.progressBar = QProgressBar(self.frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(0, 30))
        self.progressBar.setValue(24)

        self.horizontalLayout_2.addWidget(self.progressBar)


        self.verticalLayout_4.addWidget(self.frame)

        self.frame_2 = QFrame(self.conten_dowload)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)


        self.verticalLayout_4.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.conten_dowload)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_2 = QPushButton(self.frame_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setMinimumSize(QSize(90, 30))

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.frame_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(False)
        self.pushButton.setMinimumSize(QSize(90, 30))

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout_4.addWidget(self.frame_3)


        self.verticalLayout_2.addWidget(self.conten_dowload)


        self.verticalLayout.addWidget(self.background_frame_dowload)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Downloading", None))
        self.label_2.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"CANCION", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Cancel", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Exit", None))