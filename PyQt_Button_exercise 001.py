import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 400, 300)
        self.setWindowIcon(QIcon("PyQt window sample icon.png"))
        
        btn = QPushButton("Button 1", self)
        
app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()