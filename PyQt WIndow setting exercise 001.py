import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,400,300)
        
app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()
