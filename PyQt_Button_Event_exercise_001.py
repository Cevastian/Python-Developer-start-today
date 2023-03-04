# PyQt Window Button - Event connection exercise

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class QtWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 400, 300)
        self.setWindowTitle("PyQt Button Click event exercise")
        self.setWindowIcon(QIcon("PyQt window sample icon.png"))
        
        btn = QPushButton("Button 1", self)
        btn.move(10,10)
        btn.clicked.connect(self.btn_clicked)
        
    def btn_clicked(self):
        print("Button clicked")
        
app = QApplication(sys.argv)
window = QtWindow()
window.show()
app.exec_()