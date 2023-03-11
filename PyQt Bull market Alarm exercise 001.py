# PyQt with QtDesigner Bull market alarm exercise 001

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("C:\\Users\\chois\\Desktop\\PythonProject\\Codes\\Coding Exercise with Cryptocurrency Auto Trading\\Bull-Bear market Alarm 001.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
app = QApplication(sys.argv)
win = MyWindow()
win.show()
app.exec_()
