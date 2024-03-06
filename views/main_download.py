from PySide6.QtCore import QCoreApplication, QMetaObject, QSize, Qt
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtWidgets import (
    QFrame, QHBoxLayout, QLabel,
    QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout
)
from functions.path import FILE_PATH


class downloadWindow(object):
    def setupUi(self, main_download_dialog):
        if not main_download_dialog.objectName():
            main_download_dialog.setObjectName(u"main_download_dialog")
        main_download_dialog.resize(500, 200)
        main_download_dialog.setMinimumSize(QSize(500, 200))
        main_download_dialog.setMaximumSize(QSize(500, 200))
        self.horizontalLayout_3 = QHBoxLayout(main_download_dialog)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, 0, 0)
        self.background_frame_download = QFrame(main_download_dialog)
        self.background_frame_download.setObjectName(
            u"background_frame_download")
        self.background_frame_download.setFrameShape(QFrame.StyledPanel)
        self.background_frame_download.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.background_frame_download)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.conten_download = QFrame(self.background_frame_download)
        self.conten_download.setObjectName(u"conten_download")
        self.conten_download.setFrameShape(QFrame.StyledPanel)
        self.conten_download.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.conten_download)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.progresbar_frame = QFrame(self.conten_download)
        self.progresbar_frame.setObjectName(u"progresbar_frame")
        self.progresbar_frame.setFrameShape(QFrame.StyledPanel)
        self.progresbar_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.progresbar_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.img_bar = QLabel(self.progresbar_frame)
        self.img_bar.setObjectName(u"img_bar")
        self.img_bar.setMaximumSize(QSize(50, 50))
        self.img_bar.setPixmap(
            QPixmap(f"{FILE_PATH}/assets/icons/downloading.png"))
        self.img_bar.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.img_bar)

        self.progressBardownload = QProgressBar(self.progresbar_frame)
        self.progressBardownload.setObjectName(u"progressBardownload")

        self.horizontalLayout_2.addWidget(self.progressBardownload)

        self.verticalLayout_4.addWidget(self.progresbar_frame)

        self.name_frame = QFrame(self.conten_download)
        self.name_frame.setObjectName(u"name_frame")
        self.name_frame.setFrameShape(QFrame.StyledPanel)
        self.name_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.name_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.track_name = QLabel(self.name_frame)
        self.track_name.setObjectName(u"track_name")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(9)
        font.setBold(True)
        self.track_name.setFont(font)
        self.track_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.track_name)

        self.verticalLayout_4.addWidget(self.name_frame)

        self.bottons_frame = QFrame(self.conten_download)
        self.bottons_frame.setObjectName(u"bottons_frame")
        self.bottons_frame.setFrameShape(QFrame.StyledPanel)
        self.bottons_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.bottons_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_botton = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_botton)

        self.pushButton_cancel = QPushButton(self.bottons_frame)
        self.pushButton_cancel.setObjectName(u"pushButton_cancel")
        self.pushButton_cancel.setEnabled(False)
        self.pushButton_cancel.setMinimumSize(QSize(90, 30))

        self.horizontalLayout.addWidget(self.pushButton_cancel)

        self.pushButton_exit = QPushButton(self.bottons_frame)
        self.pushButton_exit.setObjectName(u"pushButton_exit")
        self.pushButton_exit.setEnabled(False)
        self.pushButton_exit.setMinimumSize(QSize(90, 30))

        self.horizontalLayout.addWidget(self.pushButton_exit)

        self.verticalLayout_4.addWidget(self.bottons_frame)

        self.verticalLayout_2.addWidget(self.conten_download)

        self.horizontalLayout_3.addWidget(self.background_frame_download)

        self.retranslateUi(main_download_dialog)

        QMetaObject.connectSlotsByName(main_download_dialog)

    def retranslateUi(self, main_download_dialog):
        main_download_dialog.setWindowTitle(QCoreApplication.translate(
            "main_download_dialog", u"To download", None))
        self.img_bar.setText("")
        self.track_name.setText("")
        self.pushButton_cancel.setText(QCoreApplication.translate(
            "main_download_dialog", u"Cancel", None))
        self.pushButton_exit.setText(QCoreApplication.translate(
            "main_download_dialog", u"Exit", None))
