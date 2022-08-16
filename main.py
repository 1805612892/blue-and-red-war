#!/usr/bin/python#-*-coding:utf-8-*-
import sys

from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QApplication

from map import Set_map

class game:
    """初始化"""
    def __init__(self):
        self.land = map_init()
        # self.thread = listen_thread()
        # self.thread.start()
        self.listen()
    """监听鼠标事件"""
    def listen(self):
        button = self.land.cache
        self.sign = 0

        for i in range(len(button)):
            button[i].clicked.connect(self.record)
            # print(button[i].note)
            # if self.sign == 0:
            #     self.site = None
            #     # continue
            # else:
            #     self.site = i
    """感知鼠标点击"""
    def record(self):
        send = self.sender()
        print(send.objectName())
        if self.sign == 1:
            self.sign = 0
        else:
            self.sign = 1
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

#创建游戏对象，用于监听调用
# w = game()

# class listen_thread(QThread):
#     def __init__(self):
#         super(listen_thread, self).__init__()
    # def run(self) -> None:
    #     """监听鼠标事件"""
    #     button = w.land.cache
    #     w.sign = 0
    #     while True:
    #         for i in range(len(button)):
    #             button[i].clicked.connect(w.record)
    #             print(w.sign)
    #             if w.sign == 0:
    #                 w.site = None
    #                 continue
    #             else:
    #                 w.site = i
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = game()
    w.land.show()
    # while True:
    #     print(0)
    app.exec()

