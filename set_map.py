#!/usr/bin/python#-*-coding:utf-8-*-
import sys

from PyQt5.QtWidgets import (QApplication,QWidget,QGridLayout, QPushButton,QMainWindow)

class set_map(QWidget):
    def __init__(self):
        super(set_map, self).__init__()
        # 地图初始大小
        self.size_x = 5
        self.size_y = 5
        # 地图储存
        self.cache = []
        self.init_ui()
    def init_ui(self):
        self.ui = QWidget()
        self.ui.setWindowTitle('blue and red war')
        self.grid = QGridLayout()
        self.ui.setLayout(self.grid)
        self.set()
    """创建地图"""
    def set(self):
        positions = [(i, j) for i in range(self.size_x) for j in range(self.size_y)]
        name = [(i, j) for i in range(self.size_x) for j in range(self.size_y)]
        name = map(str,name)
        for position, name in zip(positions, name):
            button = QPushButton(name)
            button.setStyleSheet("backgroud-color : blue")
            button.setGeometry(100, 100, 100, 100)
            self.grid.addWidget(button, *position)
#            self.cache.append(button)
#        for num in range(len(self.cache)):
#            self.cache[num].setGeometry(100,100,100,100)
#        self.cache[0].setStyleSheet("backgroud-color : red")
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = set_map()
    w.ui.show()
    app.exec()