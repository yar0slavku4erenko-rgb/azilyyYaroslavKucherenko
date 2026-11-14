from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
import random
from ui import Ui_MainWindow

class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.example)

    def example(self):pass

app = QApplication([])
ex = Widget()
ex.show()
app.exec_()
