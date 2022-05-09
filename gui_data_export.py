# -*- coding: utf-8 -*-

# form implementation generated from reading ui file '.\gui_data_export.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate, Qt
from io import StringIO
import pandas as pd
from data import data
import resource


dept_list = [
    '请选择',
    '研发一部',
    '研发二部',
    '研发三部',
]


class UiDataDump(object):
    def __init__(self, form):
        self.vertical_layout = QtWidgets.QVBoxLayout(form)
        self.horizontal_layout_5 = QtWidgets.QHBoxLayout()
        self.label = QtWidgets.QLabel(form)
        self.horizontal_layout_7 = QtWidgets.QHBoxLayout()
        self.label_4 = QtWidgets.QLabel(form)
        self.combo_box_create_dept = QtWidgets.QComboBox(form)
        self.horizontal_layout = QtWidgets.QHBoxLayout()
        self.label_5 = QtWidgets.QLabel(form)
        # self.combo_box_work_kind = QtWidgets.QComboBox(form)
        self.horizontal_layout_2 = QtWidgets.QHBoxLayout()
        self.label_6 = QtWidgets.QLabel(form)
        self.date_begin_time_edit = QtWidgets.QDateEdit(form)
        self.date_end_time_edit = QtWidgets.QDateEdit(form)
        self.horizontal_layout_19 = QtWidgets.QHBoxLayout()
        self.btn_ok = QtWidgets.QPushButton(form)
        self.vertical_layout_2 = QtWidgets.QVBoxLayout()
        self.label_3 = QtWidgets.QLabel(form)
        self.label_2 = QtWidgets.QLabel(form)

        self.work_kind = pd.read_csv(StringIO(data), dtype=str)

    def setup(self, form):
        current_date = QDate.currentDate()
        
        form.setObjectName("form")
        form.resize(854, 600)

        self.vertical_layout.setObjectName("vertical_layout")

        self.horizontal_layout_5.setObjectName("horizontal_layout_5")
        spacer_item = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_5.addItem(spacer_item)

        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.horizontal_layout_5.addWidget(self.label)
        spacer_item1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_5.addItem(spacer_item1)
        self.vertical_layout.addLayout(self.horizontal_layout_5)
        spacer_item2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.vertical_layout.addItem(spacer_item2)

        self.horizontal_layout_7.setContentsMargins(-1, 0, -1, 0)
        self.horizontal_layout_7.setObjectName("horizontal_layout_7")
        spacer_item3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_7.addItem(spacer_item3)

        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(size_policy)
        self.label_4.setMinimumSize(QtCore.QSize(0, 0))

        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)

        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.horizontal_layout_7.addWidget(self.label_4)
        spacer_item4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_7.addItem(spacer_item4)

        # 部
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.combo_box_create_dept.sizePolicy().hasHeightForWidth())
        self.combo_box_create_dept.setSizePolicy(size_policy)
        self.combo_box_create_dept.setMinimumSize(QtCore.QSize(200, 35))
        self.combo_box_create_dept.setObjectName("comboBox")

        # 设置录入机构字体
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.combo_box_create_dept.setFont(font)

        self.combo_box_create_dept.setEditable(True)

        # 数据初始化
        for dept in dept_list:
            self.combo_box_create_dept.addItem(dept)

        self.horizontal_layout_7.addWidget(self.combo_box_create_dept)
        spacer_item5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_7.addItem(spacer_item5)
        self.vertical_layout.addLayout(self.horizontal_layout_7)

        self.horizontal_layout.setContentsMargins(-1, 0, -1, 0)
        self.horizontal_layout.setObjectName("horizontal_layout")
        spacer_item6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout.addItem(spacer_item6)

        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        # label5 类别
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.horizontal_layout.addWidget(self.label_5)
        spacer_item7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout.addItem(spacer_item7)

        # 类别
        self.tree_widget_work_kind = QtWidgets.QTreeWidget(form)

        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.tree_widget_work_kind.sizePolicy().hasHeightForWidth())
        self.tree_widget_work_kind.setSizePolicy(size_policy)
        self.tree_widget_work_kind.setMinimumSize(QtCore.QSize(300, 350))

        self.tree_widget_work_kind.setObjectName("tree_widget_work_kind")
        self.tree_widget_work_kind.setColumnWidth(0, 120)

        '''
        item_0 = QtWidgets.QTreeWidgetItem(self.tree_widget_work_kind)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.tree_widget_work_kind)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_0 = QtWidgets.QTreeWidgetItem(self.tree_widget_work_kind)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        '''
        df = self.work_kind
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
                print(second_name)
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
                    print(last, second_name)

        self.horizontal_layout.addWidget(self.tree_widget_work_kind)

        spacer_item8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout.addItem(spacer_item8)
        self.vertical_layout.addLayout(self.horizontal_layout)

        self.horizontal_layout_2.setContentsMargins(-1, 0, -1, 0)
        self.horizontal_layout_2.setObjectName("horizontal_layout_2")
        spacer_item9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_2.addItem(spacer_item9)

        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.horizontal_layout_2.addWidget(self.label_6)

        # 开始时间

        # self.date_begin_time_edit = QtWidgets.QDateTimeEdit(form)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.date_begin_time_edit.sizePolicy().hasHeightForWidth())
        self.date_begin_time_edit.setSizePolicy(size_policy)
        self.date_begin_time_edit.setMinimumSize(QtCore.QSize(200, 35))

        # 设置开始时间的默认时间
        self.date_begin_time_edit.setDate(current_date)

        self.date_begin_time_edit.setCalendarPopup(True)
        self.date_begin_time_edit.setObjectName("date_begin_time_edit")
        self.date_begin_time_edit.setDisplayFormat('yyyy-MM-dd')
        self.horizontal_layout_2.addWidget(self.date_begin_time_edit)

        # 结束时间
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.date_end_time_edit.sizePolicy().hasHeightForWidth())
        self.date_end_time_edit.setSizePolicy(size_policy)
        self.date_end_time_edit.setMinimumSize(QtCore.QSize(200, 35))
        self.date_end_time_edit.setCalendarPopup(True)

        self.date_end_time_edit.setObjectName("date_end_time_edit")
        self.date_end_time_edit.setDisplayFormat('yyyy-MM-dd')
        
        # 设置结束时间的默认时间
        self.date_end_time_edit.setDate(current_date)
        self.horizontal_layout_2.addWidget(self.date_end_time_edit)

        spacer_item10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_2.addItem(spacer_item10)
        self.vertical_layout.addLayout(self.horizontal_layout_2)
        spacer_item11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vertical_layout.addItem(spacer_item11)

        self.horizontal_layout_19.setContentsMargins(-1, 0, -1, 0)
        self.horizontal_layout_19.setObjectName("horizontal_layout_19")
        spacer_item12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_19.addItem(spacer_item12)

        self.btn_ok.setMinimumSize(QtCore.QSize(50, 55))
        self.btn_ok.setObjectName("btn_ok")
        self.horizontal_layout_19.addWidget(self.btn_ok)
        spacer_item13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_19.addItem(spacer_item13)
        self.vertical_layout.addLayout(self.horizontal_layout_19)
        spacer_item14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vertical_layout.addItem(spacer_item14)

        self.vertical_layout_2.setContentsMargins(-1, 0, -1, 0)
        self.vertical_layout_2.setObjectName("vertical_layout_2")

        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.vertical_layout_2.addWidget(self.label_3)

        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.vertical_layout_2.addWidget(self.label_2)
        self.vertical_layout.addLayout(self.vertical_layout_2)
        spacer_item15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vertical_layout.addItem(spacer_item15)

        self.retranslate(form)
        QtCore.QMetaObject.connectSlotsByName(form)
        # 链接槽函数
        self.tree_widget_work_kind.itemChanged.connect(self.handle_changed)

    def retranslate(self, form):
        _translate = QtCore.QCoreApplication.translate
        form.setWindowTitle(_translate("form", "数据比对v1.0"))
        self.label.setText(_translate("form", "数据导出"))
        self.label_4.setText(_translate("form", "部"))
        self.label_5.setText(_translate("form", "类别"))

        self.tree_widget_work_kind.headerItem().setText(0, _translate("Form", "类别"))
        self.label_6.setText(_translate("form", "    录入时间"))
        self.btn_ok.setText(_translate("form", "确定"))
        self.label_3.setText(_translate("form", "注:"))
        self.label_2.setText(_translate("form", "数据比对完成之后，会有比对完成的弹出框提示，并且将会在比对源文件的同级目录下生成一个比对文件。"))

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