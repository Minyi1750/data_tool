# -*- coding: utf-8 -*-

# form implementation generated from reading ui file 'C:\Users\gzgb\Desktop\minyi\gb\gui_data_export._newui3.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from data import dept, data
from io import StringIO
import pandas as pd
import resource


class UiDataDump(object):
    def setup(self, form):
        form.setObjectName("form")
        form.resize(855, 740)

        self.verticalLayout = QtWidgets.QVBoxLayout(form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.label = QtWidgets.QLabel(form)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.label_5 = QtWidgets.QLabel(form)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_7.addWidget(self.label_5)
        self.tree_widget_work_kind = QtWidgets.QTreeWidget(form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tree_widget_work_kind.sizePolicy().hasHeightForWidth())
        self.tree_widget_work_kind.setSizePolicy(sizePolicy)
        self.tree_widget_work_kind.setMinimumSize(QtCore.QSize(300, 300))
        self.tree_widget_work_kind.setObjectName("tree_widget_work_kind")

        df = pd.read_csv(StringIO(data), dtype=str)
        first_menu = df[df['parent_id'] == '0']['name'].tolist()
        work_kind_dict = {}

        # 一级菜单
        for first in first_menu:
            first_item = QtWidgets.QTreeWidgetItem(self.tree_widget_work_kind)
            first_item.setText(0, first)
            first_item.setCheckState(0, Qt.Unchecked)
            work_kind_dict[first] = first_item

            # 二级菜单
            first_menu_id = df[df['name'] == first]['id'].tolist()[0]
            second_menu_names = df[df['parent_id'] == first_menu_id]['name'].tolist()
            for second_name in second_menu_names:
                # print(second_name)
                second_menu_item = QtWidgets.QTreeWidgetItem(first_item)
                second_menu_item.setText(0, second_name)
                second_menu_item.setCheckState(0, Qt.Unchecked)

                # 三级菜单
                # 获取id
                last_menu_id = df[df['name'] == second_name]['id'].tolist()[0]
                # 获取id对应的name
                last_menu = df[df['parent_id'] == last_menu_id]['name'].tolist()
                if len(last_menu) == 0:
                    continue
                for last in last_menu:
                    last_menu_item = QtWidgets.QTreeWidgetItem(second_menu_item)
                    last_menu_item.setText(0, last)
                    last_menu_item.setCheckState(0, Qt.Unchecked)
                    # print(last, second_name)

        self.horizontalLayout_7.addWidget(self.tree_widget_work_kind)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.label_4 = QtWidgets.QLabel(form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)

        self.combo_box_create_dept = QtWidgets.QComboBox(form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_box_create_dept.sizePolicy().hasHeightForWidth())
        self.combo_box_create_dept.setSizePolicy(sizePolicy)
        self.combo_box_create_dept.setMinimumSize(QtCore.QSize(300, 35))
        font = QtGui.QFont()
        font.setFamily("Angsana New")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.combo_box_create_dept.setFont(font)
        self.combo_box_create_dept.setEditable(True)
        self.combo_box_create_dept.setObjectName("combo_box_create_dept")

        # 初始化机构
        for i in dept:
            self.combo_box_create_dept.addItem(i)

        self.horizontalLayout_2.addWidget(self.combo_box_create_dept)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem7)
        self.label_6 = QtWidgets.QLabel(form)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_19.addWidget(self.label_6)
        self.date_edit_begin_time = QtWidgets.QDateEdit(form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.date_edit_begin_time.sizePolicy().hasHeightForWidth())
        self.date_edit_begin_time.setSizePolicy(sizePolicy)
        self.date_edit_begin_time.setMinimumSize(QtCore.QSize(147, 35))
        self.date_edit_begin_time.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 8, 26), QtCore.QTime(0, 0, 0)))
        self.date_edit_begin_time.setCalendarPopup(True)
        self.date_edit_begin_time.setObjectName("date_edit_begin_time")
        self.horizontalLayout_19.addWidget(self.date_edit_begin_time)

        self.date_edit_end_time = QtWidgets.QDateEdit(form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.date_edit_end_time.sizePolicy().hasHeightForWidth())
        self.date_edit_end_time.setSizePolicy(sizePolicy)
        self.date_edit_end_time.setMinimumSize(QtCore.QSize(147, 35))
        self.date_edit_end_time.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 8, 26), QtCore.QTime(0, 0, 0)))
        self.date_edit_end_time.setCalendarPopup(True)
        self.date_edit_end_time.setObjectName("date_edit_end_time")
        self.horizontalLayout_19.addWidget(self.date_edit_end_time)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem8)
        self.verticalLayout.addLayout(self.horizontalLayout_19)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem9)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem10)
        self.btn_ok = QtWidgets.QPushButton(form)
        self.btn_ok.setMinimumSize(QtCore.QSize(50, 50))
        self.btn_ok.setObjectName("btn_ok")
        self.horizontalLayout_4.addWidget(self.btn_ok)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem11)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem12)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(form)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_2 = QtWidgets.QLabel(form)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_7 = QtWidgets.QLabel(form)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem13)

        self.retranslate(form)
        QtCore.QMetaObject.connectSlotsByName(form)
        # 链接槽函数
        self.tree_widget_work_kind.itemChanged.connect(self.handle_changed)

    def retranslate(self, form):
        _translate = QtCore.QCoreApplication.translate
        form.setWindowTitle(_translate("form", "数据比对v1.0"))
        self.label.setText(_translate("form", "数据导出"))
        self.label_5.setText(_translate("form", "类别"))
        self.tree_widget_work_kind.headerItem().setText(0, _translate("form", "类别"))

        self.label_4.setText(_translate("form", "部门"))

        self.label_6.setText(_translate("form", "录入时间"))
        self.btn_ok.setText(_translate("form", "确定"))
        self.label_3.setText(_translate("form", "注:"))
        self.label_2.setText(_translate("form", "数据导出完成之后，会有导出完成的弹出框提示，并且将会程序执行目录下生成一个比对文件。"))
        self.label_7.setText(_translate("form", "类别为必选项，部门如果不选择，则相当于全选。"))

    def handle_changed(self, item, column):
        # 获取选中节点的子节点个数
        count = item.childCount()
        # 如果被选中
        if item.checkState(column) == Qt.Checked:
            # 连同下面子子节点全部设置为选中状态
            for f in range(count):
                if item.child(f).checkState(0) != Qt.Checked:
                    item.child(f).setCheckState(0, Qt.Checked)
        # 如果取消选中
        if item.checkState(column) == Qt.Unchecked:
            # 连同下面子子节点全部设置为取消选中状态
            for f in range(count):
                if item.child(f).checkState != Qt.Unchecked:
                    item.child(f).setCheckState(0, Qt.Unchecked)

