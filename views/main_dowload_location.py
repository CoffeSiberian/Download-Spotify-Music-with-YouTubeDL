from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class DowloadLocation(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 200)
        Form.setMinimumSize(QSize(400, 200))
        Form.setMaximumSize(QSize(400, 200))
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.background_frame_location = QFrame(Form)
        self.background_frame_location.setObjectName(u"background_frame_location")
        self.background_frame_location.setFrameShape(QFrame.StyledPanel)
        self.background_frame_location.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.background_frame_location)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_conten_location = QFrame(self.background_frame_location)
        self.frame_conten_location.setObjectName(u"frame_conten_location")
        self.frame_conten_location.setFrameShape(QFrame.StyledPanel)
        self.frame_conten_location.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_conten_location)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 10, 341, 41))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.frame_conten_location)

        self.frame = QFrame(self.background_frame_location)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(300, 25))
        self.lineEdit.setMaximumSize(QSize(300, 25))

        self.horizontalLayout_4.addWidget(self.lineEdit)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.background_frame_location)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_3 = QPushButton(self.frame_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.setMinimumSize(QSize(90, 30))
        self.pushButton_3.setMaximumSize(QSize(90, 30))
        icon = QIcon()
        icon.addFile(u"./assets/icons/diskette.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.pushButton_3)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.background_frame_location)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Select download location", None))
        self.lineEdit.setText(QCoreApplication.translate("Form", u"c:/location", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"Save", None))