#!/usr/bin/python#-*-coding:utf-8-*-
import sys
import random

# from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QDialog

from map import SetMap

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
# print(2222222222)
# class onetest(set_map):
#     def __init__(self):
#         print(555)
#         super(onetest,self).__init__()
#         self.cache[0].setStyleSheet("background-color : red")
#         print(111)

# print(222222)
# class map_init(Set_map):
#     def __init__(self):
#         super(map_init, self).__init__()
#         self.define_terrain()
#     """扩展地图"""
#     def extend_map(self):
#         pass
#     """地形设置"""
#     def define_terrain(self):
#         self.chess_name = str((random.randint(0,self.size_x - 1),random.randint(0,self.size_y - 1)))
#         print(self.chess_name)
# """pyqt的奇怪bug，只可以在类内或者QApp内调用它子类的属性/方法"""
# print(9999)
# app = QApplication(sys.argv)
# w = map_init()
# print(w)
# w.show()
# app.exec()
# app = QApplication(sys.argv)
# w = main_window()
# w.ui.show()
# app.exec()
# """玩家信息"""
# class player():
#     def __init__(self,player_number):
#         # 储存身分组信息
#         self.id = None
#         self.flag = ['red','blue','yellow']
#         self.player_chess(player_number)
#     """玩家的棋子信息"""
#     def player_chess(self,player_number):
#         id = []
#         for i in range(player_number):
#             id.append(i)
#         self.id = zip(id,self.flag)
#         for x in self.id:
#             print(x)
#
# game = player(2)
# a = [[], []]
# a[0].append(1)
# print(a)
chess_layout_1 = [(3, 0), (4, 1), (3, 3), (2, 0), (4, 2)]
chess_layout_2 = [(y, x) for (x, y) in chess_layout_1]
print(chess_layout_2)
