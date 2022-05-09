# coding=utf-8
"""

"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPalette, QBrush, QPixmap
from PyQt5.QtCore import pyqtSlot
import cx_Oracle

# 主界面
from gui_form import UiMainWindow
# 数据比对界面
from gui_main_data_compare import MyDataCompareWidget
# 数据导出界面
from gui_main_data_dump import MyDataDumpWidget
# 部门
from gui_organization_dump_main import MyOrganizationDumpWidget
# 飘窗展示
from gui_window_update_main import MyWindowUpdateWidget
# 系统重启
from gui_system_reboot_main import MySystemRebootWidget


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = UiMainWindow(self)
        self.ui.setup(self)

        self.palette = QPalette()
        self.palette.setBrush(QPalette.Background, QBrush(QPixmap(":/images/bj_main.png")))
        self.setPalette(self.palette)

        # 是否应该在main window与data compare之上重新创建一个class?
        # 数据比对界面
        self.data_compare = MyDataCompareWidget()
        # 人员导出
        self.data_dump = MyDataDumpWidget()
        # 部门
        self.organization_dump = MyOrganizationDumpWidget()

        # 飘窗展示
        self.window_update = MyWindowUpdateWidget()

        # 飘窗展示
        self.system_reboot = MySystemRebootWidget()

    # 切换到数据比对界面
    @pyqtSlot()
    def on_btn_data_compare_clicked(self):
        # self.hide()
        self.data_compare.show()

    # 切换到数据导出界面 人员导出
    @pyqtSlot()
    def on_btn_data_output_clicked(self):
        # self.hide()
        self.data_dump.show()

    # 切换到部门界面
    @pyqtSlot()
    def on_btn_organization_dump_clicked(self):
        # self.hide()
        self.organization_dump.show()

    # 切换到飘窗展示 btn_leader_show
    @pyqtSlot()
    def on_btn_leader_show_clicked(self):
        # self.hide()
        self.window_update.show()

    # 切换到系统重启 btn_system_reboot
    @pyqtSlot()
    def on_btn_system_reboot_clicked(self):
        # self.hide()
        self.system_reboot.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    '''
    Form.setStyleSheet("#Form { background: rgba(32, 80, 96, 100);border-image: url(:/images/bj_main.png);}")
    '''
    widget = MainWindow()
    widget.show()

    sys.exit(app.exec())
