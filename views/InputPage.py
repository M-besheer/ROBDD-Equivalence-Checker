# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'InputPage.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_INPUT(object):
    def setupUi(self, INPUT):
        if not INPUT.objectName():
            INPUT.setObjectName(u"INPUT")
        INPUT.resize(800, 500)
        INPUT.setMaximumSize(QSize(800, 500))
        self.centralwidget = QWidget(INPUT)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 60, 111, 16))
        font = QFont()
        font.setFamilies([u"Century Gothic"])
        font.setPointSize(11)
        font.setBold(True)
        self.label.setFont(font)
        self.Vorder2 = QComboBox(self.centralwidget)
        self.Vorder2.setObjectName(u"Vorder2")
        self.Vorder2.setGeometry(QRect(560, 200, 121, 24))
        self.Vorder2.setEditable(True)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(410, 200, 151, 20))
        self.label_4.setFont(font)
        self.Calcul = QPushButton(self.centralwidget)
        self.Calcul.setObjectName(u"Calcul")
        self.Calcul.setEnabled(True)
        self.Calcul.setGeometry(QRect(530, 390, 151, 41))
        self.Calcul.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.Calcul.setAutoDefault(False)
        self.Calcul.setFlat(False)
        self.savef2 = QPushButton(self.centralwidget)
        self.savef2.setObjectName(u"savef2")
        self.savef2.setGeometry(QRect(590, 120, 81, 31))
        self.Func2 = QLineEdit(self.centralwidget)
        self.Func2.setObjectName(u"Func2")
        self.Func2.setGeometry(QRect(240, 120, 341, 31))
        self.savef1 = QPushButton(self.centralwidget)
        self.savef1.setObjectName(u"savef1")
        self.savef1.setGeometry(QRect(590, 50, 81, 31))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(120, 130, 111, 16))
        self.label_2.setFont(font)
        self.Func1 = QLineEdit(self.centralwidget)
        self.Func1.setObjectName(u"Func1")
        self.Func1.setGeometry(QRect(240, 50, 341, 31))
        self.Func1.setAutoFillBackground(False)
        self.Vorder1 = QComboBox(self.centralwidget)
        self.Vorder1.setObjectName(u"Vorder1")
        self.Vorder1.setGeometry(QRect(269, 200, 111, 24))
        self.Vorder1.setAcceptDrops(True)
        self.Vorder1.setEditable(True)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(110, 200, 151, 20))
        self.label_3.setFont(font)
        self.Error1 = QLabel(self.centralwidget)
        self.Error1.setObjectName(u"Error1")
        self.Error1.setGeometry(QRect(240, 90, 521, 16))
        self.Error1.setScaledContents(True)
        self.Error2 = QLabel(self.centralwidget)
        self.Error2.setObjectName(u"Error2")
        self.Error2.setGeometry(QRect(240, 160, 531, 16))
        self.Error2.setScaledContents(True)
        INPUT.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(INPUT)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        INPUT.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(INPUT)
        self.statusbar.setObjectName(u"statusbar")
        INPUT.setStatusBar(self.statusbar)

        self.retranslateUi(INPUT)

        QMetaObject.connectSlotsByName(INPUT)
    # setupUi

    def retranslateUi(self, INPUT):
        INPUT.setWindowTitle(QCoreApplication.translate("INPUT", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("INPUT", u"Function 1:", None))
        self.label_4.setText(QCoreApplication.translate("INPUT", u"Variable ordering 2:", None))
        self.Calcul.setText(QCoreApplication.translate("INPUT", u"Calculate Equivalence", None))
        self.savef2.setText(QCoreApplication.translate("INPUT", u"Save F2", None))
        self.Func2.setPlaceholderText(QCoreApplication.translate("INPUT", u"Enter the second boolean function", None))
        self.savef1.setText(QCoreApplication.translate("INPUT", u"Save F1", None))
        self.label_2.setText(QCoreApplication.translate("INPUT", u"Function 2:", None))
        self.Func1.setPlaceholderText(QCoreApplication.translate("INPUT", u"Enter the first boolean function", None))
        self.label_3.setText(QCoreApplication.translate("INPUT", u"Variable ordering 1:", None))
        self.Error1.setText("")
        self.Error2.setText("")
    # retranslateUi

