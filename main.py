#!/usr/bin/python#-*-coding:utf-8-*-
import sys
import random

from PyQt5.QtWidgets import QApplication

from map import Set_map

"""游戏主体"""
class game():

    """初始化"""
    def __init__(self):
        self.land = map_init()
        self.init_extend_map()
        self.listen()

    """扩展地图初始化"""
    def init_extend_map(self):
        self.land.define_terrain()
        #禁止通过地形
        self.disable = []
        self.chess = self.land.chess_name
        self.check(sign=1)

    """建立鼠标监听事件"""
    def listen(self):
        for button in self.land.cache:
            button.clicked.connect(self.record)

    """判断点击来源"""
    def record(self):
        send = self.land.sender()
        self.chess = send.text()
        self.check()

    """检查移动条件"""
    def check(self,sign = 0):
        site = None
        for i in range(len(self.land.cache)):
            if self.land.cache[i].text() == self.chess:# and self.land.cache[i] != disable
                site = i
                #遍历禁止地形
                for disable in self.disable:
                    if self.land.cache[i] == disable:
                        site = None
        #安全检查通过，允许进军
        if site != None:
            #检查为人类棋子
            if sign == 0:
                #回合判定
                if True:
                    self.march(site)
            #检查为高山地形
            if sign == 1:
                self.flag(self.land.cache[site],'green')
                self.disable.append(self.land.cache[site])

    """棋子移动"""
    def march(self,site):
        # 安全检查通过，允许进军
        if site != None:
        #持续隐藏字体
            self.flag(self.land.cache[site],'red')

    """棋子染色"""
    def flag(self,object,color):
        object.setStyleSheet("color : rgb(0,0,0,0);\n"
                                 "background-color : {}".format(color))

"""玩家信息"""
class player():
    def __init__(self,player_number):
        # 储存身分组信息
        self.id = None
        self.flag = ['red','blue','yellow']
        self.player_chess(player_number)
    """玩家的棋子信息"""
    def player_chess(self,player_number):
        id = []
        for i in range(player_number):
            id.append(i)
        self.id = zip(id,self.flag)


"""地图初始化"""
class map_init(Set_map):
    def __init__(self):
        super(map_init, self).__init__()
    """扩展地图"""
    def extend_map(self):
        pass
    """随机位置生成一座高山"""
    def define_terrain(self):
        self.chess_name = str((random.randint(0,self.size_x - 1),random.randint(0,self.size_y - 1)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = game()
    w.land.show()
    app.exec()

