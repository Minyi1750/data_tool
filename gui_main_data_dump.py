"""
    Purpose: 数据导出功能界面，由主界面点击进入
    Author: MinYi
    Create Time: 2021.08.27
"""
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QTreeWidgetItemIterator
from PyQt5.QtCore import pyqtSlot, Qt
from datetime import datetime
from gui_data_dump import UiDataDump
from PyQt5.QtGui import QPalette, QBrush, QPixmap

from sqlalchemy import create_engine
from sqlalchemy.types import String
import pandas as pd
import sys
import cx_Oracle

time_format = '%Y-%m-%d %H:%M:%S'
# oracle_clint_dir = './oracle_client/instantclient_11_2'
# cx_Oracle.init_oracle_client(lib_dir=oracle_clint_dir)


def get_connection():
    database_type = 'oracle'
    host = '127.0.0.1'
    port = '1521'
    user = 'example'
    password = 'example'
    database = 'example'
    url_template = "{database_type}://{user}:{password}@{host}:{port}/{database}"

    url = url_template.format(
        database_type=database_type,
        user=user,
        password=password,
        host=host,
        port=port,
        database=database
    )

    engine = create_engine(url, encoding='utf8', echo=True)

    return engine


class MyDataDumpWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = UiDataDump()
        self.ui.setup(self)

        self.palette = QPalette()
        self.palette.setBrush(QPalette.Background, QBrush(QPixmap(":/images/bj_main.png")))
        self.setPalette(self.palette)

    @pyqtSlot()
    def on_btn_ok_clicked(self):
        title = '数据导出'
        info = '是否确定数据导出？\n部门: {dept}\n类别: {work_kind}\n时间范围: {date_range}'
        sql_list = ['Select * From Person where 1 = 1']
        work_kind_list = []

        iterator = QTreeWidgetItemIterator(self.ui.tree_widget_work_kind)
        while iterator.value():
            item = iterator.value()
            if item.checkState(0) == Qt.Checked:
                column_count = item.columnCount()
                for i in range(column_count):
                    text = item.text(i)
                    '''
                    if i == column_count - 1:
                        print(text)
                    else:
                        print(text, end=' ')
                    '''
                    work_kind_list.append(text)
            iterator.__iadd__(1)

        dept = self.ui.combo_box_create_dept.currentText()
        if dept != '请选择':
            sql_list.append('''and "部门" = '{}' '''.format(dept))

        begin_date = self.ui.date_edit_begin_time.dateTime()
        begin_date_sec = begin_date.toTime_t()
        if begin_date_sec is not None:
            sql_list.append('''and  to_number("数据库录入时间") > {} '''.format(begin_date_sec))

        end_date = self.ui.date_edit_end_time.dateTime()
        end_date_sec = end_date.toTime_t()
        if end_date_sec is not None:
            sql_list.append('''and  to_number("数据库录入时间") < {} '''.format(end_date_sec))

        if len(work_kind_list) != 0:
            sql_list.append('''and "类别" in ('{}'''.format("','".join(work_kind_list)))

            sql = ' '.join(sql_list) + "')" + ''' order by to_number("数据库录入时间") desc'''
        else:
            sql = ' '.join(sql_list) + ''' order by to_number("数据库录入时间") desc'''

        default_btn = QMessageBox.NoButton

        t = self.ui.date_edit_begin_time.text() + ' - ' + self.ui.date_edit_end_time.text()

        result = QMessageBox.question(self, title, info.format(dept='全部' if dept == '请选择' else dept,
                                                               work_kind=','.join(work_kind_list),
                                                               date_range=t),
                                      QMessageBox.Yes | QMessageBox.Cancel | QMessageBox.No,
                                      default_btn)
        if result == QMessageBox.Yes:
            if len(work_kind_list) == 0:
                QMessageBox.information(self, '类别为空', '类别为必选项，可以单选、多选、或全选！')
                return

            print('{} INFO 人员导出 begin'.format(datetime.now().strftime(time_format)))

            engine = get_connection()
            print('{} INFO execute sql begin'.format(datetime.now().strftime(time_format)))
            data = pd.read_sql(sql, con=engine)
            output_file_name = './人员导出{}.xlsx'.format(datetime.now().strftime('%Y%m%d%H%M%S'))
            print('{} INFO execute sql end'.format(datetime.now().strftime(time_format)))

            print('{} INFO write to excel begin'.format(datetime.now().strftime(time_format)))
            data.to_excel(output_file_name)
            print('{} INFO write to excel end'.format(datetime.now().strftime(time_format)))

            print('{} INFO 人员导出 end'.format(datetime.now().strftime(time_format)))
            QMessageBox.information(self, '比对结果', '比对完成\n文件名: {}'.format(output_file_name))

        elif result == QMessageBox.Cancel or result == QMessageBox.No:
            print('撤销')

    @pyqtSlot()
    def on_tree_widget_work_kind_changed(self, item, column):
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyDataDumpWidget()
    widget.show()

    sys.exit(app.exec())
