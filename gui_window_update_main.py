"""
    Purpose: 部门功能界面，由主界面点击进入
    Author: MinYi
    Create Time: 2021.08.27
"""
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QFileDialog
from PyQt5.QtCore import pyqtSlot, QDir
from datetime import datetime
from gui_window_update_ui import UiWindowUpdate
from PyQt5.QtGui import QPalette, QBrush, QPixmap
import sys
from fabric import Connection
from os.path import basename

time_format = '%Y-%m-%d %H:%M:%S'


def update_app_window(window_name, is_on_off, window_id, window_content, photo_name):

    host = '127.0.0.1'
    user = 'example'
    port = 7799
    password = {'password': 'professional=6dd'}

    now = datetime.now().strftime('%Y%m%d%H%M%S')
    target_id = None
    if window_name == '飘窗1':
        target_id = 'update_app_one'
    elif window_name == '飘窗2':
        target_id = 'update_app_two'
    else:
        target_id = 'no_target_id'

    is_open = None
    if is_on_off == '开':
        is_open = 'close'
    elif is_on_off == '关':
        is_open = 'open'
    else:
        print('no support')
        return 1

    # sh update_app_window.sh update_app_one close 18 上级通知
    command_template = 'sh /home/noah/app/coweb/gui/coweb/cms/portal/' \
                       'update_app_window.sh {id} {is_open} {target_id} {target_name}'
    command = command_template.format(
        id=target_id,
        is_open=is_open,
        target_id='no_window_id' if len(window_id) < 1 else window_id,
        target_name='no_window_content' if len(window_content) < 1 else window_content)
    c = Connection(host=host, user=user, port=port, connect_kwargs=password)
    # sh update_app_window.sh update_app_one close 18 上级通知
    print(command)
    c.run(command, encoding='utf-8', hide=True)

    if is_on_off != '关':
        target_photo_name = None
        if window_name == '飘窗1':
            target_photo_name = 'indexLogo.jpg'
        elif window_name == '飘窗2':
            target_photo_name = 'indexLogo1.jpg'
        else:
            target_photo_name = 'no_photo'

        file_name = basename(photo_name)
        dir_name = '/home/noah/app/coweb/gui/coweb/cms/portal'

        c.put(photo_name, '/tmp')
        shell = 'mv {dir_name}/{target_photo_name} {dir_name}/{target_photo_name}_{now}'.format(
            dir_name=dir_name,
            target_photo_name=target_photo_name,
            now=now
        )
        print(shell)
        c.run(shell)

        shell = 'mv /tmp/{file_name} {dir_name}/{target_photo_name}'.format(
            file_name=file_name,
            dir_name=dir_name,
            target_photo_name=target_photo_name)
        print(shell)
        c.run(shell)
    print('end')


class MyWindowUpdateWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = UiWindowUpdate()
        self.ui.setup(self)

        self.palette = QPalette()
        self.palette.setBrush(QPalette.Background, QBrush(QPixmap(":/images/bj_main.png")))
        self.setPalette(self.palette)

        self.photo_name = None

    @pyqtSlot()
    def on_btn_photo_upload_clicked(self):
        # QMessageBox.information(self, 'information 消息框', '是否上传文件')
        cur_path = QDir.currentPath()
        title = '选择文件'
        file_name, filter_used = QFileDialog.getOpenFileName(self, title, cur_path, filter='*.jpg')
        now = datetime.now().strftime(time_format)
        print(f'{now} INFO {file_name} {filter_used}')
        self.ui.line_edit_link_photo.setText(file_name)
        self.photo_name = file_name

    @pyqtSlot()
    def on_btn_ok_clicked(self):
        title = '飘窗更新'
        info_template = '是否确定更新指定窗口？\n' \
                        '窗口名: {window_name}\n' \
                        '窗口开关: {is_on_off}\n' \
                        '链接ID: {window_id}\n' \
                        '链接栏目: {window_content}\n' \
                        '图片: {photo_name}'
        window_name = self.ui.combo_box_window_number.currentText().strip()
        is_on_off = self.ui.combo_box_close_on_off.currentText().strip()
        window_id = self.ui.line_edit_link_id.text().strip()
        window_content = self.ui.line_edit_link_content.text().strip()

        # window_photo = self.ui.line_edit_link_photo.get
        # print(window_name, is_on_off, window_id, window_content)

        if is_on_off == '请选择':
            QMessageBox.warning(self, '请选择开或关', '窗口开关为必选项，请选择开或关，不能是请选择状态')
            return 1

        if window_name == '请选择':
            QMessageBox.warning(self, '请选择开或关', '窗口名为必选项，请选择窗口名，不能是请选择状态')
            return 1

        info = info_template.format(
            window_name=window_name,
            is_on_off=is_on_off,
            window_id='无' if len(window_id) < 1 else window_id,
            window_content='无' if len(window_content) < 1 else window_content,
            photo_name=self.photo_name
        )
        default_btn = QMessageBox.NoButton
        result = QMessageBox.question(self, title, info,
                                      QMessageBox.Yes | QMessageBox.Cancel | QMessageBox.No,
                                      default_btn)
        if is_on_off == '开':
            if len(self.ui.line_edit_link_photo.text()) < 1 or len(window_id) < 1 or len(window_content) < 1:
                QMessageBox.warning(self, '不能为空', '链接ID、链接栏目、图片不能为空')
                return 1

        if result == QMessageBox.Yes:
            print('开始更新')
            # window_name, is_on_off, window_id, window_content, photo_name
            print('13;', window_name, is_on_off, window_id, window_content, self.photo_name)
            update_app_window(window_name, is_on_off, window_id, window_content, self.photo_name)
            QMessageBox.information(self, '更新完成', '飘窗更新完成')

        elif result == QMessageBox.Cancel or result == QMessageBox.No:
            print('{} INFO 撤销'.format(datetime.now().strftime(time_format)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWindowUpdateWidget()
    widget.show()

    sys.exit(app.exec())
