# PyQt Bull market Alarm exercise 004

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
import pybithumb

tickers = ["BTC", "ETH", "XRP", "ADA"]
form_class = uic.loadUiType("C:\\Users\\chois\\Desktop\\PythonProject\\Codes\\Coding Exercise with Cryptocurrency Auto Trading\\Bull-Bear market Alarm 001.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        timer = QTimer(self)
        timer.start(3000)
        timer.timeout.connect(self.timeout)
        
    def get_market_infos(self, ticker):
        df = pybithumb.get_ohlcv(ticker)
        ma5 = df['close'].rolling(window=5).mean()
        last_ma5 = ma5[-2]
        price = pybithumb.get_current_price(ticker)
        
        state = None
        if price > last_ma5:
            state = "Bull market"
        else:
            state = "Bear market"
        
        return price, last_ma5, state
    
    def timeout(self):
        for i, ticker in enumerate(tickers):
            item = QTableWidgetItem(ticker)
            self.PyQt_tableWidget.setItem(i, 0, item)
            
            price, last_ma5, state = self.get_market_infos(ticker)
            self.PyQt_tableWidget.setItem(i, 1, QTableWidgetItem(str(price)))
            self.PyQt_tableWidget.setItem(i, 2, QTableWidgetItem(str(last_ma5)))
            self.PyQt_tableWidget.setItem(i, 3, QTableWidgetItem(str(state)))
            
app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()
          
               
    
