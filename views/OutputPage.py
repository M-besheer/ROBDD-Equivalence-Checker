# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'OutputPage.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)
import resources_rc

class Ui_Output(object):
    def setupUi(self, Output):
        if not Output.objectName():
            Output.setObjectName(u"Output")
        Output.resize(800, 400)
        Output.setMinimumSize(QSize(800, 400))
        Output.setMaximumSize(QSize(800, 400))
        Output.setWindowOpacity(1.000000000000000)
        self.centralwidget = QWidget(Output)
        self.centralwidget.setObjectName(u"centralwidget")
        self.equiv = QLabel(self.centralwidget)
        self.equiv.setObjectName(u"equiv")
        self.equiv.setGeometry(QRect(210, 10, 311, 51))
        font = QFont()
        font.setFamilies([u"Century Gothic"])
        font.setPointSize(11)
        font.setBold(True)
        self.equiv.setFont(font)
        self.equiv.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.equiv.setWordWrap(True)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 120, 101, 21))
        self.label_3.setFont(font)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(540, 157, 101, 21))
        self.label_4.setFont(font)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 160, 101, 21))
        self.label_5.setFont(font)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(560, 110, 101, 21))
        self.label_6.setFont(font)
        self.ShowBDD1 = QPushButton(self.centralwidget)
        self.ShowBDD1.setObjectName(u"ShowBDD1")
        self.ShowBDD1.setGeometry(QRect(130, 113, 81, 31))
        self.ShowBDD1.setFont(font)
        self.ShowBDD1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.ShowBDD2 = QPushButton(self.centralwidget)
        self.ShowBDD2.setObjectName(u"ShowBDD2")
        self.ShowBDD2.setGeometry(QRect(650, 100, 81, 31))
        self.ShowBDD2.setFont(font)
        self.ShowBDD2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.ShowROBDD1 = QPushButton(self.centralwidget)
        self.ShowROBDD1.setObjectName(u"ShowROBDD1")
        self.ShowROBDD1.setGeometry(QRect(130, 160, 81, 31))
        self.ShowROBDD1.setFont(font)
        self.ShowROBDD1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.ShowROBDD2 = QPushButton(self.centralwidget)
        self.ShowROBDD2.setObjectName(u"ShowROBDD2")
        self.ShowROBDD2.setGeometry(QRect(650, 150, 81, 31))
        self.ShowROBDD2.setFont(font)
        self.ShowROBDD2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.TryAgain = QPushButton(self.centralwidget)
        self.TryAgain.setObjectName(u"TryAgain")
        self.TryAgain.setGeometry(QRect(370, 310, 101, 31))
        self.TryAgain.setFont(font)
        self.TryAgain.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.lable7 = QLabel(self.centralwidget)
        self.lable7.setObjectName(u"lable7")
        self.lable7.setGeometry(QRect(10, 310, 361, 31))
        self.lable7.setFont(font)
        self.lable7.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lable7.setFrameShape(QFrame.Shape.NoFrame)
        self.lable7.setFrameShadow(QFrame.Shadow.Plain)
        self.lable7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.spongebob = QLabel(self.centralwidget)
        self.spongebob.setObjectName(u"spongebob")
        self.spongebob.setGeometry(QRect(260, 80, 231, 171))
        self.spongebob.setFont(font)
        self.spongebob.setPixmap(QPixmap(u":/Images/Images/sad_spongebob.png"))
        self.spongebob.setScaledContents(True)
        self.spongebob.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.spongebob.setWordWrap(True)
        self.Function1 = QLabel(self.centralwidget)
        self.Function1.setObjectName(u"Function1")
        self.Function1.setGeometry(QRect(0, 30, 251, 31))
        self.Function1.setFont(font)
        self.Function1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Function1.setWordWrap(True)
        self.Function2 = QLabel(self.centralwidget)
        self.Function2.setObjectName(u"Function2")
        self.Function2.setGeometry(QRect(560, 20, 181, 51))
        self.Function2.setFont(font)
        self.Function2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Function2.setWordWrap(True)
        self.Vorder1 = QLabel(self.centralwidget)
        self.Vorder1.setObjectName(u"Vorder1")
        self.Vorder1.setGeometry(QRect(0, 70, 251, 31))
        self.Vorder1.setFont(font)
        self.Vorder1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Vorder1.setWordWrap(True)
        self.Vorder2 = QLabel(self.centralwidget)
        self.Vorder2.setObjectName(u"Vorder2")
        self.Vorder2.setGeometry(QRect(560, 50, 181, 51))
        self.Vorder2.setFont(font)
        self.Vorder2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Vorder2.setWordWrap(True)
        Output.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Output)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        Output.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Output)
        self.statusbar.setObjectName(u"statusbar")
        Output.setStatusBar(self.statusbar)

        self.retranslateUi(Output)

        QMetaObject.connectSlotsByName(Output)
    # setupUi

    def retranslateUi(self, Output):
        Output.setWindowTitle(QCoreApplication.translate("Output", u"MainWindow", None))
        self.equiv.setText(QCoreApplication.translate("Output", u"<To be shown>", None))
        self.label_3.setText(QCoreApplication.translate("Output", u"Show BDD1", None))
        self.label_4.setText(QCoreApplication.translate("Output", u"Show ROBDD2", None))
        self.label_5.setText(QCoreApplication.translate("Output", u"Show ROBDD1", None))
        self.label_6.setText(QCoreApplication.translate("Output", u"Show BDD2", None))
        self.ShowBDD1.setText(QCoreApplication.translate("Output", u"SHOW", None))
        self.ShowBDD2.setText(QCoreApplication.translate("Output", u"SHOW", None))
        self.ShowROBDD1.setText(QCoreApplication.translate("Output", u"SHOW", None))
        self.ShowROBDD2.setText(QCoreApplication.translate("Output", u"SHOW", None))
        self.TryAgain.setText(QCoreApplication.translate("Output", u"TRY AGAIN", None))
        self.lable7.setText(QCoreApplication.translate("Output", u"Would like to try again with different functions?", None))
        self.spongebob.setText("")
        self.Function1.setText(QCoreApplication.translate("Output", u"<To be shown>", None))
        self.Function2.setText(QCoreApplication.translate("Output", u"<To be shown>", None))
        self.Vorder1.setText(QCoreApplication.translate("Output", u"<To be shown>", None))
        self.Vorder2.setText(QCoreApplication.translate("Output", u"<To be shown>", None))
    # retranslateUi

