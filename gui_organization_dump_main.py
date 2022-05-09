"""
    Purpose: 部门功能界面，由主界面点击进入
    Author: MinYi
    Create Time: 2021.08.27
"""
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QTreeWidgetItemIterator
from PyQt5.QtCore import pyqtSlot, Qt
from datetime import datetime
from gui_organization_dump_ui import UiOrganizationDump
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


class MyOrganizationDumpWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = UiOrganizationDump()
        self.ui.setup(self)

        self.palette = QPalette()
        self.palette.setBrush(QPalette.Background, QBrush(QPixmap(":/images/bj_main.png")))
        self.setPalette(self.palette)

    def organization_dump(self):
        print('')
        print('{} INFO data dump begin'.format(datetime.now().strftime(time_format)))
        df = pd.read_excel(self.file_name, header=0, dtype=str)
        df.to_sql('temp_id_card', con=get_connection(), index=False, dtype={'zjhm': String(100)})

    @pyqtSlot()
    def on_btn_ok_clicked(self):
        title = '部门'
        info = '是否确定部门？\n部门: {dept}\n时间范围: {date_range}'
        sql_list = ['Select * From organization where 1 = 1']

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

        sql = ' '.join(sql_list) + ''' order by to_number("数据库录入时间") desc'''
        # print(sql)

        t = self.ui.date_edit_begin_time.text() + ' - ' + self.ui.date_edit_end_time.text()
        default_btn = QMessageBox.NoButton
        result = QMessageBox.question(self, title, info.format(dept='全部' if dept == '请选择' else dept,
                                                               date_range=t),
                                      QMessageBox.Yes | QMessageBox.Cancel | QMessageBox.No,
                                      default_btn)
        if result == QMessageBox.Yes:
            print('{} INFO 部门 begin'.format(datetime.now().strftime(time_format)))
            engine = get_connection()

            print('{} INFO execute sql begin'.format(datetime.now().strftime(time_format)))
            data = pd.read_sql(sql, con=engine)
            output_file_name = './部门_{}.xlsx'.format(datetime.now().strftime('%Y%m%d%H%M%S'))
            print('{} INFO execute sql end'.format(datetime.now().strftime(time_format)))

            print('{} INFO write to excel begin'.format(datetime.now().strftime(time_format)))
            data.to_excel(output_file_name)
            print('{} INFO write to excel begin'.format(datetime.now().strftime(time_format)))

            print('{} INFO 部门 end'.format(datetime.now().strftime(time_format)))
            QMessageBox.information(self, '比对结果', '比对完成\n文件名: {}'.format(output_file_name))

        elif result == QMessageBox.Cancel or result == QMessageBox.No:
            print('{} INFO 撤销'.format(datetime.now().strftime(time_format)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyOrganizationDumpWidget()
    widget.show()

    sys.exit(app.exec())
