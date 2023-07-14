from UI.Ui_demo import Ui_MainWindow
from data import ReadData
from draw import Draw3D
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QHeaderView, QLabel, QLineEdit
from PyQt5.QtGui import QTextCursor, QStandardItem, QIcon, QStandardItemModel
from PyQt5.QtCore import Qt

from threading import Thread


import sys
import os
import logging

logger = logging.getLogger(__name__)


class UiMain(Ui_MainWindow):
    def __init__(self, MainWindow) -> None:
        super().__init__()
        super().setupUi(MainWindow)
        self.reinit()
        self.bind()

    def reinit(self):
        """重新设置某些控件属性或添加新属性"""
        pass
        self.reader = ReadData()
        self._model = QStandardItemModel()
        self.treeView.setModel(self._model)
        self._model.setHorizontalHeaderLabels(["文件", "类型"])
        self.treeView.setColumnWidth(0, 500)
        generateDirectoryTree(self._model.invisibleRootItem(), r"E:\A_CODE\tutu\data")

    def bind(self):
        """绑定槽和信号"""
        pass
        self.pushButton.clicked.connect(self.thead_draw)

    def thead_draw(self):
        t1 = Thread(target=self.draw)
        t1.start()

    def draw(self):
        draw = Draw3D()
        items = get_checked_items(self._model.invisibleRootItem())
        logger.info(len(items))
        print(len(items))
        if len(items) < 1:
            return
        try:
            for item in items:
                data = item.data(Qt.UserRole)
                lines = self.reader.read_file(data)
                draw.add_lines(lines=lines, filename=data)
            draw.show()
            logger.info("succeful")
        except Exception as e:
            print(e)


def generateDirectoryTree(rootItem, directoryPath):
    subs = os.listdir(directoryPath)
    for sub in subs:
        childItem = QStandardItem(sub)
        # childItem.setIcon(QIcon(":/icons/folder.png"))  # 可选：设置图标
        childItem.setData(os.path.join(directoryPath, sub), Qt.UserRole)  # 将目录路径存储在用户角色中
        childItem.setEditable(False)
        childItem.setCheckable(True)
        rootItem.appendRow(childItem)
        if os.path.isdir(os.path.join(directoryPath, sub)):
            childItem.setCheckable(False)
            generateDirectoryTree(childItem, os.path.join(directoryPath, sub))


def get_checked_items(item):
    checked_items = []

    # 检查当前项是否被选中
    if item.checkState() == Qt.Checked:
        checked_items.append(item)  # 将当前项的数据添加到已选中项列表中

    # 遍历当前项的子项
    for row in range(item.rowCount()):
        child_item = item.child(row)
        checked_items.extend(get_checked_items(child_item))  # 递归调用获取子项的已选中项

    return checked_items

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindows = QMainWindow()
    Ui = UiMain(MainWindows)
    MainWindows.show()
    sys.exit(app.exec_())
