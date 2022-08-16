#!/usr/bin/python#-*-coding:utf-8-*-
import sys

# from PyQt5 import uic
from PyQt5.QtWidgets import QApplication,QDialog

from map import Set_map

# class main_window(QDialog):
#     def __init__(self):
#         super().__init__()
#         self.init_ui()
#     def init_ui(self):
#         self.ui = uic.loadUi('./map.ui')
#         b00 = self.ui.Button00
#         b00.clicked.connect(self.go)
#     def go(self):
#         print(666)
print(2222222222)
class onetest(set_map):
    def __init__(self):
        print(555)
        super(onetest,self).__init__()
        self.cache[0].setStyleSheet("background-color : red")
        print(111)

print(222222)

"""pyqt的奇怪bug，只可以在类内或者QApp内调用它子类的属性/方法"""
print(9999)
app = QApplication(sys.argv)
w = onetest()
print(w)
w.show()
app.exec()
    # app = QApplication(sys.argv)
    # w = main_window()
    # w.ui.show()
    # app.exec()



