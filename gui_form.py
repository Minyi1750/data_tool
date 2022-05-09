# -*- coding: utf-8 -*-

# form implementation generated from reading ui file '.\gui_login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import resource


class UiMainWindow(object):
    def __init__(self, form):
        self.verticalLayout = QtWidgets.QVBoxLayout(form)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.title = QtWidgets.QLabel(form)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        # 数据比对
        self.btn_data_compare = QtWidgets.QPushButton(form)
        self.label_2 = QtWidgets.QLabel(form)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        # 人员导出
        self.btn_data_output = QtWidgets.QPushButton(form)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        # 展示
        self.btn_leader_show = QtWidgets.QPushButton(form)
        self.label_3 = QtWidgets.QLabel(form)
        self.label_4 = QtWidgets.QLabel(form)
        self.label_5 = QtWidgets.QLabel(form)

        # 部门 organization
        self.btn_organization_dump = QtWidgets.QPushButton(form)

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
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btn_data_output.setMinimumSize(QtCore.QSize(55, 55))
        self.btn_data_output.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/数据导出.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_data_output.setIcon(icon1)
        self.btn_data_output.setIconSize(QtCore.QSize(50, 50))
        self.btn_data_output.setObjectName("btn_data_output")
        self.verticalLayout_4.addWidget(self.btn_data_output)

        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        spacer_item5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacer_item5)

        self.verticalLayout_5.setObjectName("verticalLayout_5")

        self.btn_organization_dump.setMinimumSize(QtCore.QSize(55, 55))
        self.btn_organization_dump.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/督导台账.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_organization_dump.setIcon(icon2)
        self.btn_organization_dump.setIconSize(QtCore.QSize(50, 50))
        self.btn_organization_dump.setObjectName("btn_organization_dump")
        self.verticalLayout_5.addWidget(self.btn_organization_dump)

        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        spacer_item6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacer_item6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.btn_leader_show.setMinimumSize(QtCore.QSize(55, 55))
        self.btn_leader_show.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/展示.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_leader_show.setIcon(icon3)
        self.btn_leader_show.setIconSize(QtCore.QSize(50, 50))
        self.btn_leader_show.setObjectName("btn_leader_show")
        self.verticalLayout_6.addWidget(self.btn_leader_show)
        self.label_5 = QtWidgets.QLabel(form)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_6.addWidget(self.label_5)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(10, -1, 10, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.btn_system_reboot = QtWidgets.QPushButton(form)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        sizePolicy.setHeightForWidth(self.btn_system_reboot.sizePolicy().hasHeightForWidth())

        self.btn_system_reboot.setSizePolicy(sizePolicy)
        self.btn_system_reboot.setMinimumSize(QtCore.QSize(55, 55))
        self.btn_system_reboot.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/GXWJ.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_system_reboot.setIcon(icon4)
        self.btn_system_reboot.setIconSize(QtCore.QSize(50, 50))
        self.btn_system_reboot.setObjectName("btn_system_reboot")
        self.verticalLayout_2.addWidget(self.btn_system_reboot)
        self.label = QtWidgets.QLabel(form)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem9)

        self.retranslate(form)
        QtCore.QMetaObject.connectSlotsByName(form)

    def retranslate(self, form):
        _translate = QtCore.QCoreApplication.translate
        form.setWindowTitle(_translate("form", "数据比对v1.0"))
        self.title.setText(_translate("form", "工作台"))
        self.label_2.setText(_translate("form", " 数据比对"))
        self.label_3.setText(_translate("form", " 人员导出"))
        self.label_4.setText(_translate("form", " 部门"))
        self.label_5.setText(_translate("form", " 飘窗展示"))
        self.label.setText(_translate("Form", " 系统重启"))
