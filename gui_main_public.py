# coding=utf-8
"""
    Purpose: 公用版 主界面
    Author: MinYi
    Create Time: 2021.09.03
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPalette, QBrush, QPixmap
from PyQt5.QtCore import pyqtSlot

# 主界面
from gui_main_public_ui import UiMainWindowPublic
# 数据导出界面
from gui_main_data_compare import MyDataCompareWidget


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = UiMainWindowPublic(self)
        self.ui.setup(self)

        self.palette = QPalette()
        self.palette.setBrush(QPalette.Background, QBrush(QPixmap(":/images/bj_main.png")))
        self.setPalette(self.palette)

        # 数据比对
        self.data_compare = MyDataCompareWidget()

    # 切换到数据比对界面 数据比对
    @pyqtSlot()
    def on_btn_data_compare_clicked(self):
        self.data_compare.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
