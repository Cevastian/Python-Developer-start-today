# GUI Bull market alarm exercise threads version 001

from PyQt5.QtCore import *

class Worker(QThread):
    def run(self):
        while True:
            print("Hello!")
            self.sleep(1)
            
work = Worker()
