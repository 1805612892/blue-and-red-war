#!/usr/bin/python#-*-coding:utf-8-*-
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication,QDialog

class main_window(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.ui = uic.loadUi('./map.ui')
        b00 = self.ui.Button00
        b00.clicked.connect(self.go)
    def go(self):
        print(666)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = main_window()
    w.ui.show()
    app.exec()

