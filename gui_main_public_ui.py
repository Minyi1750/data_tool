# -*- coding: utf-8 -*-

# form implementation generated from reading ui file '.\gui_mainwindow_public.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import resource


class UiMainWindowPublic(object):
    def __init__(self, form):
        self.verticalLayout = QtWidgets.QVBoxLayout(form)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.title = QtWidgets.QLabel(form)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.btn_data_compare = QtWidgets.QPushButton(form)
        self.label_2 = QtWidgets.QLabel(form)

    def setup(self, form):
        form.setObjectName("form")
        form.resize(800, 600)

        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacer_item = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacer_item)

        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setStyleSheet("color: rgb(255, 255, 255);")
        self.title.setObjectName("title")
        self.horizontalLayout.addWidget(self.title)
        spacer_item1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacer_item1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacer_item2 = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacer_item2)

        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacer_item3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacer_item3)

        self.verticalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.btn_data_compare.setMinimumSize(QtCore.QSize(55, 55))
        self.btn_data_compare.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/数据比对.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_data_compare.setIcon(icon)
        self.btn_data_compare.setIconSize(QtCore.QSize(50, 50))
        self.btn_data_compare.setObjectName("btn_data_compare")
        self.verticalLayout_3.addWidget(self.btn_data_compare)

        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        spacer_item4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacer_item4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacer_item5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacer_item5)

        self.retranslate(form)
        QtCore.QMetaObject.connectSlotsByName(form)

    def retranslate(self, form):
        _translate = QtCore.QCoreApplication.translate
        form.setWindowTitle(_translate("form", "数据比对v1.0"))
        self.title.setText(_translate("form", "工作台"))
        self.label_2.setText(_translate("form", " 数据比对"))

