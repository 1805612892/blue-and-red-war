#!/usr/bin/python#-*-coding:utf-8-*-
import sys

from PyQt5.QtWidgets import QApplication

import set_map

class game:
    """初始化"""
    def init_start():
        pass

class map_init(set_map):
    def __init__(self):
        super(map, self).__init__()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = map_init()
    w.show()
    app.exec()