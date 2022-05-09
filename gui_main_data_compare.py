"""
    Purpose: 数据比对功能界面，由主界面点击进入
    Author: MinYi
    Create Time: 2021.07.05
"""
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QFileDialog
from PyQt5.QtCore import QDir, pyqtSlot
from gui_datacompare import UiDataCompare
from PyQt5.QtGui import QPalette, QBrush, QPixmap

from sqlalchemy import create_engine
from sqlalchemy.types import String
import pandas as pd
import sys

import cx_Oracle
from datetime import datetime

time_format = '%Y-%m-%d %H:%M:%S'
oracle_clint_dir = './oracle_client/instantclient_11_2'
# oracle_clint_dir = './oracle_client/64/instantclient-basic-windows.x64-11.2.0.4.0/instantclient_11_2'
# oracle_clint_dir = 'C:/Users/gzgb/PycharmProjects/pythonProject/oracle_client/' /
#                    '64/instantclient-basic-windows.x64-11.2.0.4.0/instantclient_11_2'
cx_Oracle.init_oracle_client(lib_dir=oracle_clint_dir)


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


class MyDataCompareWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = UiDataCompare()
        self.ui.setup(self)

        self.palette = QPalette()
        self.palette.setBrush(QPalette.Background, QBrush(QPixmap(":/images/bj_main.png")))
        self.setPalette(self.palette)

        self.file_name = None

    def data_compare(self):
        now = str(datetime.now().timestamp()).replace('.', '')
        table_name = f'bidui_{now}'

        compare_sql = f'''
        select xh, zjhm, c.* 
        from {table_name} a, lingshi_value b, person c 
        where a.zjhm = b.attribute_value_new 
        and   b.object_id = c.object_id 
        order by to_number(xh)
        '''

        insert_sql = f'''
        insert into bidui_history 
        select xh, zjhm, to_char(sysdate, 'YYYY-MM-DD HH24:MI:SS') as current_date 
        from {table_name}'''

        drop_table_sql = f'''
        drop table  {table_name} purge'''

        engine = get_connection()
        file_name = self.file_name

        print('{} INFO read excel file {} begin'.format(datetime.now().strftime(time_format), file_name))
        df = pd.read_excel(file_name, header=0, dtype=str)
        print('{} INFO  read excel file {} end '.format(datetime.now().strftime(time_format), file_name))

        df.columns = ['xh', 'zjhm']
        df = df.replace(r'/s+', '', regex=True)
        column_info = {'xh': String(10), 'zjhm': String(100)}

        print('{} INFO import to database begin'.format(datetime.now().strftime(time_format)))
        df.to_sql(table_name, if_exists='replace', con=engine, index=False, dtype=column_info)
        print('{} INFO  import to database en'.format(datetime.now().strftime(time_format)))

        print(' {} INFO execute sql begin'.format(datetime.now().strftime(time_format)))
        data = pd.read_sql(compare_sql, con=engine)
        output_file_name = './比对结果{}.xlsx'.format(datetime.now().strftime('%Y%m%d%H%M%S'))
        data.to_excel(output_file_name)
        print(' {} INFO execute sql end'.format(datetime.now().strftime(time_format)))

        # 缓存数据
        engine.execute(insert_sql)

        # 删除临时表
        engine.execute(drop_table_sql)

        QMessageBox.information(self, '比对结果', '比对完成/n文件名: {}'.format(output_file_name))

    @pyqtSlot()
    def on_btn_file_upload_clicked(self):
        # QMessageBox.information(self, 'information 消息框', '是否上传文件')
        cur_path = QDir.currentPath()
        title = '选择文件'
        file_name, filter_used = QFileDialog.getOpenFileName(self, title, cur_path)
        now = datetime.now().strftime(time_format)
        print(f'{now} INFO {file_name} {filter_used}')
        self.ui.line_file_name.setText(file_name)
        self.file_name = file_name

    @pyqtSlot()
    def on_btn_ok_clicked(self):
        title = '数据比对'
        info = '是否开始数据比对？'
        if len(self.ui.line_file_name.text().strip()) == 0:
            QMessageBox.warning(self, '文件为空', '请指定需要比对的数据文件')
            return

        default_btn = QMessageBox.NoButton

        result = QMessageBox.question(self, title, info,
                                      QMessageBox.Yes | QMessageBox.Cancel | QMessageBox.No,
                                      default_btn)
        if result == QMessageBox.Yes:
            # 上传文件
            print('{} INFO 开始比对'.format(datetime.now().strftime(time_format)))
            self.data_compare()
            print('{} INFO 比对完成'.format(datetime.now().strftime(time_format)))

        elif result == QMessageBox.Cancel or result == QMessageBox.No:
            print('{} INFO 撤销'.format(datetime.now().strftime(time_format)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyDataCompareWidget()
    widget.show()

    sys.exit(app.exec())
