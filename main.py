from UI.Ui_demo import Ui_MainWindow
from data import ReadData
from draw import Draw3D
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QHeaderView, QLabel, QLineEdit
from PyQt5.QtGui import QTextCursor, QStandardItem, QIcon, QStandardItemModel
from PyQt5.QtCore import Qt


import sys
import os

class UiMain(Ui_MainWindow):
    def __init__(self, MainWindow) -> None:
        super().__init__()
        super().setupUi(MainWindow)
        # 重定向 sys.stdout
        # self.stdout_orig = sys.stdout
        # sys.stdout = self
        # sys.stderr = self
        self.reinit()
        self.bind()

    def reinit(self):
        """重新设置某些控件属性或添加新属性"""
        pass
        self.reader = ReadData()
        self._model = QStandardItemModel()
        self.treeView.setModel(self._model)
        self._model.setHorizontalHeaderLabels(["文件", "类型"])
        generateDirectoryTree(self._model.invisibleRootItem(), r"E:\Code\tutu\data")

    def bind(self):
        """绑定槽和信号"""
        pass
        self.pushButton.clicked.connect(self.draw)

    def draw(self):
        index = self.treeView.currentIndex()
        data = self._model.data(index, Qt.UserRole)
        try:
            draw = Draw3D()
            lines = self.reader.read_file(data)
            print(*lines, end='\n')
            draw.add_lines(lines=lines)
            draw.show()
            print(lines)
        except Exception as e:
            print(e)


    # def write(self, text):
    #     """输出重定向方法"""
    #     # self.textEdit.append(str(text))
    #     self.textEdit.moveCursor(QTextCursor.End)
    #     self.textEdit.insertPlainText(text)
    #     self.textEdit.moveCursor(QTextCursor.End)
    #     self.textEdit.ensureCursorVisible()

    # def flush(self):
    #     """输出重定向方法"""
    #     pass

    # def closeEvent(self, event):
    #     """恢复sys.stdout"""
    #     sys.stdout = self.stdout_orig

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
            generateDirectoryTree(childItem, os.path.join(directoryPath, sub))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindows = QMainWindow()
    Ui = UiMain(MainWindows)
    MainWindows.show()
    sys.exit(app.exec_())
