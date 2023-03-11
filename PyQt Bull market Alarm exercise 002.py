# PyQt Bull market alarm exercise 002

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *

form_class = uic.loadUiType("C:\\Users\\chois\Desktop\\PythonProject\Codes\\Coding Exercise with Cryptocurrency Auto Trading\\Bull-Bear market Alarm 001.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        timer = QTimer(self)
        timer.start(3000)
        timer.timeout.connect(self.timeout)
        
    def timeout(self):
        print("3 seconds past!")

app = QApplication(sys.argv)
win = MyWindow()
win.show()
app.exec_()
