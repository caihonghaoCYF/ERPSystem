from PyQt5.QtWidgets import *
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import QCoreApplication


class ProductManage(QWidget):
    def __init__(self):
        super(ProductManage, self).__init__()
        self.initUi()

    def initUi(self):
        self.model = QStandardItemModel(4, 3)
        self.model.setHorizontalHeaderLabels(["id", "姓名", "性别"])
        self.tableView = QTableView()
        # 关联模型
        self.tableView.setModel(self.model)

        # 水平布局
        self.hlayout = QHBoxLayout()

        self.gongyingShangLabel = QLabel()
        self.gongyingShangLabel.setObjectName("gongyingShangLabel")
        self.gongyingShangLineEdit = QLineEdit()
        self.gongyingShangLineEdit.setObjectName("gongyingShangLineEdit")
        self.hlayout.addWidget(self.gongyingShangLabel)
        self.hlayout.addWidget(self.gongyingShangLineEdit)

        self.productCodeLabel = QLabel()
        self.productCodeLabel.setObjectName("productCodeLabel")
        self.productCodeLineEdit = QLineEdit()
        self.productCodeLineEdit.setObjectName("productCodeLineEdit")
        self.hlayout.addWidget(self.productCodeLabel)
        self.hlayout.addWidget(self.productCodeLineEdit)

        self.productNameLabel = QLabel()
        self.productNameLabel.setObjectName("productNameLabel")
        self.productNameLineEdit = QLineEdit()
        self.productNameLineEdit.setObjectName("productNameLineEdit")
        self.hlayout.addWidget(self.productNameLabel)
        self.hlayout.addWidget(self.productNameLineEdit)

        self.queryButton = QPushButton("查询")
        self.hlayout.addWidget(self.queryButton)

        spacerItem = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.qVBoxLayout = QVBoxLayout() #垂直布局
        self.qVBoxLayout.addSpacerItem(spacerItem)
        self.qVBoxLayout.addLayout(self.hlayout)
        self.qVBoxLayout.addWidget(self.tableView)
        self.setLayout(self.qVBoxLayout)

        item1_1 = QStandardItem("1")
        item1_2 = QStandardItem("月亮代表我的心")
        item1_3 = QStandardItem("100")
        self.model.setItem(0, 0, item1_1)
        self.model.setItem(0, 1, item1_2)
        self.model.setItem(0, 2, item1_3)
        self.retranslateUi()
    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.gongyingShangLabel.setText(_translate("Form", "供应商："))
        self.productCodeLabel.setText(_translate("Form", "商品编码："))
        self.productNameLabel.setText(_translate("Form", "商品名称："))



