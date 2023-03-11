# PyQt GUI Bull market alarm exercise 003

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *

tickers = ["BTC", "ETH", "XRP", "ADA"]
form_class = uic.loadUiType("C:\\Users\chois\\Desktop\\PythonProject\\Codes\\Coding Exercise with Cryptocurrency Auto Trading\\Bull-Bear market Alarm 001.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        timer = QTimer(self)
        timer.start(3000)
        timer.timeout.connect(self.timeout)
        
    def timeout(self):
        for i, ticker in enumerate(tickers):
            item = QTableWidgetItem(ticker)
            self.PyQt_tableWidget.setItem(i, 0, item)
            
app = QApplication(sys.argv)
win = MyWindow()
win.show()
app.exec_()
    