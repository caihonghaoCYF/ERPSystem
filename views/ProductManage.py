from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout, QPushButton, QStackedLayout


class ProductManage(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.btnPress = QPushButton("Table AAAA")
        layout = QVBoxLayout()
        self.setLayout(layout)
        layout.addWidget(self.btnPress)
        self.setStyleSheet("background-color:green;")
