#!/usr/bin/python#-*-coding:utf-8-*-
import sys

from PyQt5.QtWidgets import QApplication

from map import Set_map

class game():
    """初始化"""
    def __init__(self):
        self.land = map_init()
        self.listen()
    def listen(self):
        for button in self.land.cache:
            button.clicked.connect(self.record)
    """感知鼠标点击"""
    def record(self):
        send = self.land.sender()
        print(send.text())
    """检查移动条件"""
    def check(self):
        pass
    """棋子移动"""
    def move(self):
        self.check()
        if self.site != None:
            self.land.cache[self.site].setStyleSheet("background-color : red")

class player():
    pass

class map_extend():
    """扩展地图"""
    def extend_map(self):
        pass
    """地形设置"""
    def define_terrain(self):
        pass


class map_init(Set_map):
    def __init__(self):
        super(map_init, self).__init__()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = game()
    w.land.show()
    app.exec()

