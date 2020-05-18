from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout, QPushButton, QTableView
from PyQt5.QtGui import QStandardItemModel


class CategoryManage(QWidget):
    def __init__(self):
        super(CategoryManage, self).__init__()
        self.initUi()

    def initUi(self):
        self.model = QStandardItemModel(4, 3)
        self.model.setHorizontalHeaderLabels(["id", "姓名2", "性别2"])
        self.tableView = QTableView()
        # 关联模型
        self.tableView.setModel(self.model)

        layout = QVBoxLayout() #垂直布局
        layout.addWidget(self.tableView)
        self.setLayout(layout)





