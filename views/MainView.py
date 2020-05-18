from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class MainMenu(QMainWindow):
    def __init__(self):
        super(MainMenu, self).__init__()
        bar = self.menuBar()  # 获取菜单栏
        file = bar.addMenu("文件")
        save = QAction("保存")
        save.setShortcut("Ctrl + S")
        file.addAction(save)
        save.triggered.connect(self.process)

    def process(self, a):
        print("test")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainMenu()
    main.show()
    sys.exit(app.exec())
