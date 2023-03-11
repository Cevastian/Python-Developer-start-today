# GUI Bull market alarm exercise threads version 002

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Worker(QThread):
    def run(self):
        while True:
            print("Hello!")
            self.sleep(1)
            
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.worker = Worker()
        self.worker.start()
        
app = QApplication(sys.argv)
mywindow = MyWindow()
mywindow.show()
app.exec_()
