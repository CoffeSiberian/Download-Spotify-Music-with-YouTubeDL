from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCommandLinkButton, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class SpotifyConfig(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        Form.setMinimumSize(QSize(400, 300))
        Form.setMaximumSize(QSize(400, 300))
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.background_frame_api = QFrame(Form)
        self.background_frame_api.setObjectName(u"background_frame_api")
        self.background_frame_api.setFrameShape(QFrame.StyledPanel)
        self.background_frame_api.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.background_frame_api)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.background_frame_api)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 50))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(30, 30))
        self.label_4.setMaximumSize(QSize(30, 30))
        self.label_4.setPixmap(QPixmap(u"./assets/icons/spotify.png"))
        self.label_4.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(16)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setMargin(3)

        self.horizontalLayout_4.addWidget(self.label_3)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)


        self.verticalLayout_4.addWidget(self.frame_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.label_2)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(250, 30))

        self.verticalLayout_2.addWidget(self.lineEdit)

        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(250, 30))

        self.verticalLayout_2.addWidget(self.lineEdit_2)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_2 = QPushButton(self.frame_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setMinimumSize(QSize(90, 30))
        self.pushButton_2.setMaximumSize(QSize(90, 30))
        icon = QIcon()
        icon.addFile(u"./assets/icons/diskette.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.pushButton_2)


        self.verticalLayout_4.addWidget(self.frame_3)


        self.verticalLayout_5.addWidget(self.frame)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.frame_2 = QFrame(self.background_frame_api)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 6, 6)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.gitHub = QCommandLinkButton(self.frame_2)
        self.gitHub.setObjectName(u"gitHub")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gitHub.sizePolicy().hasHeightForWidth())
        self.gitHub.setSizePolicy(sizePolicy)
        self.gitHub.setMaximumSize(QSize(160, 16777215))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(9)
        font2.setBold(True)
        self.gitHub.setFont(font2)
        self.gitHub.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u"./assets/icons/question.png", QSize(), QIcon.Normal, QIcon.Off)
        self.gitHub.setIcon(icon1)
        self.gitHub.setIconSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.gitHub)


        self.verticalLayout_5.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.background_frame_api)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_4.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"Spotify API KEY", None))
        self.label.setText(QCoreApplication.translate("Form", u"Client ID", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Client Secret", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Save", None))
        self.gitHub.setText(QCoreApplication.translate("Form", u"How to get API KEY", None))