from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, QSize, Qt
from PySide6.QtGui import QFont, QIcon
from PySide6.QtWidgets import (
    QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QVBoxLayout
)


class downloadLocation(object):
    def setupUi(self, main_downloadlocation_dialog):
        if not main_downloadlocation_dialog.objectName():
            main_downloadlocation_dialog.setObjectName(
                u"main_downloadlocation_dialog")
        main_downloadlocation_dialog.resize(400, 200)
        main_downloadlocation_dialog.setMinimumSize(QSize(400, 200))
        main_downloadlocation_dialog.setMaximumSize(QSize(400, 200))
        self.horizontalLayout = QHBoxLayout(main_downloadlocation_dialog)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.background_frame_location = QFrame(main_downloadlocation_dialog)
        self.background_frame_location.setObjectName(
            u"background_frame_location")
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
        self.title_cfg_label = QLabel(self.frame_conten_location)
        self.title_cfg_label.setObjectName(u"title_cfg_label")
        self.title_cfg_label.setGeometry(QRect(30, 10, 341, 41))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(16)
        font.setBold(True)
        self.title_cfg_label.setFont(font)
        self.title_cfg_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.frame_conten_location)

        self.text_input_frame = QFrame(self.background_frame_location)
        self.text_input_frame.setObjectName(u"text_input_frame")
        self.text_input_frame.setFrameShape(QFrame.StyledPanel)
        self.text_input_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.text_input_frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lineEdit_location = QLineEdit(self.text_input_frame)
        self.lineEdit_location.setObjectName(u"lineEdit_location")
        self.lineEdit_location.setMinimumSize(QSize(300, 25))
        self.lineEdit_location.setMaximumSize(QSize(300, 25))

        self.horizontalLayout_4.addWidget(self.lineEdit_location)

        self.verticalLayout_2.addWidget(self.text_input_frame)

        self.botton_save_frame = QFrame(self.background_frame_location)
        self.botton_save_frame.setObjectName(u"botton_save_frame")
        self.botton_save_frame.setFrameShape(QFrame.StyledPanel)
        self.botton_save_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.botton_save_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_save = QPushButton(self.botton_save_frame)
        self.pushButton_save.setObjectName(u"pushButton_save")
        self.pushButton_save.setEnabled(True)
        self.pushButton_save.setMinimumSize(QSize(90, 30))
        self.pushButton_save.setMaximumSize(QSize(90, 30))
        icon = QIcon()
        icon.addFile(u"assets/icons/diskette.png",
                     QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_save.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.pushButton_save)

        self.verticalLayout_2.addWidget(self.botton_save_frame)

        self.horizontalLayout.addWidget(self.background_frame_location)

        self.retranslateUi(main_downloadlocation_dialog)

        QMetaObject.connectSlotsByName(main_downloadlocation_dialog)

    def retranslateUi(self, main_downloadlocation_dialog):
        main_downloadlocation_dialog.setWindowTitle(QCoreApplication.translate(
            "main_downloadlocation_dialog", u"Select download folder", None))
        self.title_cfg_label.setText(QCoreApplication.translate(
            "main_downloadlocation_dialog", u"Select download location", None))
        self.lineEdit_location.setText(QCoreApplication.translate(
            "main_downloadlocation_dialog", u"c:/location", None))
        self.pushButton_save.setText(QCoreApplication.translate(
            "main_downloadlocation_dialog", u"Save", None))
