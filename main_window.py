# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QGridLayout, QHBoxLayout,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QRadioButton, QSizePolicy, QStatusBar, QTextEdit,
    QTimeEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(229, 320)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gl_tasks = QGridLayout()
        self.gl_tasks.setObjectName(u"gl_tasks")

        self.verticalLayout.addLayout(self.gl_tasks)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tb_new_task_title = QLineEdit(self.centralwidget)
        self.tb_new_task_title.setObjectName(u"tb_new_task_title")
        font = QFont()
        font.setPointSize(16)
        self.tb_new_task_title.setFont(font)

        self.horizontalLayout.addWidget(self.tb_new_task_title)

        self.btn_new_task = QPushButton(self.centralwidget)
        self.btn_new_task.setObjectName(u"btn_new_task")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_new_task.sizePolicy().hasHeightForWidth())
        self.btn_new_task.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(20)
        self.btn_new_task.setFont(font1)
        self.btn_new_task.setStyleSheet(u"background-color:green")

        self.horizontalLayout.addWidget(self.btn_new_task)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.date_box = QDateEdit(self.centralwidget)
        self.date_box.setObjectName(u"date_box")
        self.date_box.setDate(QDate(2023, 1, 1))

        self.verticalLayout.addWidget(self.date_box)

        self.time_box = QTimeEdit(self.centralwidget)
        self.time_box.setObjectName(u"time_box")

        self.verticalLayout.addWidget(self.time_box)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"border:no-border")
        self.lineEdit.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.lineEdit)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.radioButton_normal = QRadioButton(self.centralwidget)
        self.radioButton_normal.setObjectName(u"radioButton_normal")
        self.radioButton_normal.setStyleSheet(u"background-color:pink;")
        self.radioButton_normal.setChecked(True)

        self.horizontalLayout_3.addWidget(self.radioButton_normal)

        self.radioButton_high = QRadioButton(self.centralwidget)
        self.radioButton_high.setObjectName(u"radioButton_high")
        self.radioButton_high.setStyleSheet(u"background-color:red")

        self.horizontalLayout_3.addWidget(self.radioButton_high)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addLayout(self.verticalLayout_3)

        self.tb_new_task_description = QTextEdit(self.centralwidget)
        self.tb_new_task_description.setObjectName(u"tb_new_task_description")
        self.tb_new_task_description.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.tb_new_task_description)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 229, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.tb_new_task_title.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter task here", None))
        self.btn_new_task.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"Priority:", None))
        self.radioButton_normal.setText(QCoreApplication.translate("MainWindow", u"normal", None))
        self.radioButton_high.setText(QCoreApplication.translate("MainWindow", u"high", None))
        self.tb_new_task_description.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter description here", None))
    # retranslateUi

