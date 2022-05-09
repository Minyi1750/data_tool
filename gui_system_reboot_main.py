"""
    Purpose: 部门功能界面，由主界面点击进入
    Author: MinYi
    Create Time: 2021.08.27
"""
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QFileDialog
from PyQt5.QtCore import pyqtSlot, QDir
from datetime import datetime
from gui_system_reboot_ui import UiSystemReboot
from PyQt5.QtGui import QPalette, QBrush, QPixmap
import sys
from fabric import Connection

time_format = '%Y-%m-%d %H:%M:%S'

command_info = [
    {
        'name': '重启界面服务',
        'host': '192.168.56.110',
        'user': 'demo',
        'port': 22,
        'password': {'password': 'demo'},
        'command': 'sh /home/tomcat_restart.sh',
    },
    {
        'name': '关闭Oracle数据库',
        'host': '192.168.56.112',
        'user': 'demo',
        'port': 22,
        'password': {'password': 'demo'},
        'command': 'sh /home/oracle_stop_db.sh',
    },
    {
        'name': '启动Oracle数据库',
        'host': '192.168.56.110',
        'user': 'demo',
        'port': 22,
        'password': {'password': 'demo'},
        'command': 'sh /home/oracle_start_db.sh',
    },
]


def execute(item_name):
    info = None
    for i in command_info:
        if i['name'] == item_name:
            info = i
            break

    host = info['host']
    user = info['user']
    port = info['port']
    connect_kwargs = info['password']
    command = info['command']

    # print(host, user, port, connect_kwargs, command)
    with Connection(host=host, user=user, port=port, connect_kwargs=connect_kwargs) as c:
        # print(command)
        c.run(command, encoding='utf-8')


class MySystemRebootWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = UiSystemReboot()
        self.ui.setup(self)

        self.palette = QPalette()
        self.palette.setBrush(QPalette.Background, QBrush(QPixmap(":/images/bj_main.png")))
        self.setPalette(self.palette)

        self.photo_name = None

    @pyqtSlot()
    def on_btn_ok_clicked(self):
        title = '系统重启'
        info_template = '是否确定确定执行如下项目？\n' \
                        '项目名: {item_name}'
        item_name = self.ui.combo_box_window_number.currentText().strip()

        if item_name == '请选择':
            QMessageBox.warning(self, '请选择开或关', '请选择需要执行的项目')
            return 1

        info = info_template.format(item_name=item_name)
        default_btn = QMessageBox.NoButton
        result = QMessageBox.question(self, title, info,
                                      QMessageBox.Yes | QMessageBox.Cancel | QMessageBox.No,
                                      default_btn)

        if result == QMessageBox.Yes:
            execute(item_name)
            QMessageBox.information(self, '执行完成', '命令执行完成')
        elif result == QMessageBox.Cancel or result == QMessageBox.No:
            print('{} INFO 撤销'.format(datetime.now().strftime(time_format)))
        else:
            print('撤销')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MySystemRebootWidget()
    widget.show()

    sys.exit(app.exec())
