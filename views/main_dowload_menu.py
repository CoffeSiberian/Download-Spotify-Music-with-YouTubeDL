from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class DowloadMenuLink(object):
    def setupUi(self, dowload_menu_link):
        if not dowload_menu_link.objectName():
            dowload_menu_link.setObjectName(u"dowload_menu_link")
        dowload_menu_link.resize(400, 200)
        dowload_menu_link.setMinimumSize(QSize(400, 200))
        dowload_menu_link.setMaximumSize(QSize(400, 200))
        self.verticalLayout = QVBoxLayout(dowload_menu_link)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.background_frame_link = QFrame(dowload_menu_link)
        self.background_frame_link.setObjectName(u"background_frame_link")
        self.background_frame_link.setFrameShape(QFrame.StyledPanel)
        self.background_frame_link.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.background_frame_link)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.text_info_frame = QFrame(self.background_frame_link)
        self.text_info_frame.setObjectName(u"text_info_frame")
        self.text_info_frame.setFrameShape(QFrame.StyledPanel)
        self.text_info_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.text_info_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.text_info_frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)


        self.verticalLayout_3.addWidget(self.text_info_frame)

        self.link_frame = QFrame(self.background_frame_link)
        self.link_frame.setObjectName(u"link_frame")
        self.link_frame.setFrameShape(QFrame.StyledPanel)
        self.link_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.link_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.link_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(30, 30))
        self.label_2.setMaximumSize(QSize(30, 30))
        self.label_2.setPixmap(QPixmap(u"./assets/icons/link.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_2)

        self.lineEdit = QLineEdit(self.link_frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(290, 30))
        self.lineEdit.setMaximumSize(QSize(0, 0))

        self.horizontalLayout.addWidget(self.lineEdit)


        self.horizontalLayout_3.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addWidget(self.link_frame)

        self.frame_3 = QFrame(self.background_frame_link)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButton_2 = QPushButton(self.frame_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setMinimumSize(QSize(90, 30))

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.frame_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(True)
        self.pushButton.setMinimumSize(QSize(90, 30))

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.verticalLayout_3.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.background_frame_link)


        self.retranslateUi(dowload_menu_link)

        QMetaObject.connectSlotsByName(dowload_menu_link)

    def retranslateUi(self, dowload_menu_link):
        dowload_menu_link.setWindowTitle(QCoreApplication.translate("dowload_menu_link", u"Dowload", None))
        self.label.setText(QCoreApplication.translate("dowload_menu_link", u"Paste your Spotify Link", None))
        self.label_2.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("dowload_menu_link", u"Dowload", None))
        self.pushButton.setText(QCoreApplication.translate("dowload_menu_link", u"Cancel", None))