from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_main_dowload_dialog(object):
    def setupUi(self, main_dowload_dialog):
        if not main_dowload_dialog.objectName():
            main_dowload_dialog.setObjectName(u"main_dowload_dialog")
        main_dowload_dialog.resize(500, 200)
        main_dowload_dialog.setMinimumSize(QSize(500, 200))
        main_dowload_dialog.setMaximumSize(QSize(500, 200))
        self.horizontalLayout_3 = QHBoxLayout(main_dowload_dialog)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, 0, 0)
        self.background_frame_dowload = QFrame(main_dowload_dialog)
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
        self.progresbar_frame = QFrame(self.conten_dowload)
        self.progresbar_frame.setObjectName(u"progresbar_frame")
        self.progresbar_frame.setFrameShape(QFrame.StyledPanel)
        self.progresbar_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.progresbar_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.img_bar = QLabel(self.progresbar_frame)
        self.img_bar.setObjectName(u"img_bar")
        self.img_bar.setMaximumSize(QSize(50, 50))
        self.img_bar.setPixmap(QPixmap(u"./assets/icons/downloading.png"))
        self.img_bar.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.img_bar)

        self.progressBardowload = QProgressBar(self.progresbar_frame)
        self.progressBardowload.setObjectName(u"progressBardowload")
        self.progressBardowload.setMinimumSize(QSize(0, 30))
        self.progressBardowload.setValue(24)

        self.horizontalLayout_2.addWidget(self.progressBardowload)


        self.verticalLayout_4.addWidget(self.progresbar_frame)

        self.name_frame = QFrame(self.conten_dowload)
        self.name_frame.setObjectName(u"name_frame")
        self.name_frame.setFrameShape(QFrame.StyledPanel)
        self.name_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.name_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.track_name = QLabel(self.name_frame)
        self.track_name.setObjectName(u"track_name")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(14)
        font.setBold(True)
        self.track_name.setFont(font)
        self.track_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.track_name)


        self.verticalLayout_4.addWidget(self.name_frame)

        self.bottons_frame = QFrame(self.conten_dowload)
        self.bottons_frame.setObjectName(u"bottons_frame")
        self.bottons_frame.setFrameShape(QFrame.StyledPanel)
        self.bottons_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.bottons_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_botton = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_botton)

        self.pushButton_cancel = QPushButton(self.bottons_frame)
        self.pushButton_cancel.setObjectName(u"pushButton_cancel")
        self.pushButton_cancel.setEnabled(True)
        self.pushButton_cancel.setMinimumSize(QSize(90, 30))

        self.horizontalLayout.addWidget(self.pushButton_cancel)

        self.pushButton_exit = QPushButton(self.bottons_frame)
        self.pushButton_exit.setObjectName(u"pushButton_exit")
        self.pushButton_exit.setEnabled(False)
        self.pushButton_exit.setMinimumSize(QSize(90, 30))

        self.horizontalLayout.addWidget(self.pushButton_exit)


        self.verticalLayout_4.addWidget(self.bottons_frame)


        self.verticalLayout_2.addWidget(self.conten_dowload)


        self.horizontalLayout_3.addWidget(self.background_frame_dowload)


        self.retranslateUi(main_dowload_dialog)

        QMetaObject.connectSlotsByName(main_dowload_dialog)

    def retranslateUi(self, main_dowload_dialog):
        main_dowload_dialog.setWindowTitle(QCoreApplication.translate("main_dowload_dialog", u"Dialog", None))
        self.img_bar.setText("")
        self.track_name.setText(QCoreApplication.translate("main_dowload_dialog", u"CANCION", None))
        self.pushButton_cancel.setText(QCoreApplication.translate("main_dowload_dialog", u"Cancel", None))
        self.pushButton_exit.setText(QCoreApplication.translate("main_dowload_dialog", u"Exit", None))