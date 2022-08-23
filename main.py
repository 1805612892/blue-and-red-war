#!/usr/bin/python#-*-coding:utf-8-*-
import sys
import random

from PyQt5.QtWidgets import QApplication

from map import SetMap


class Game():
    """游戏主体"""

    def __init__(self):
        """初始化"""
        self.land = MapInit()
        self.player = Player(2)
        self.init_extend_map()
        self.listen()


    def init_extend_map(self):
        """
        扩展地图初始化
        """
        self.land.define_terrain()
        # 禁止通过地形
        self.disable = []
        self.map_load(self.land.chess_name, 1)
        # 导入军队初始布局
        self.map_load(self.land.chess_layout_1, 2)
        self.map_load(self.land.chess_layout_2, 3)

    def map_load(self, context, sign):
        """
        :param context: 导入地图的棋子名称
        :param sign 导入功能的check的sign值
        """
        if isinstance(context, str):
            self.chess = context
            self.check(sign)
        else:
            for name in context:
                self.chess = name
                self.check(sign)
    def listen(self):
        """
        建立鼠标监听事件
        """
        for button in self.land.cache:
            button.clicked.connect(self.record)

    def record(self):
        """
        判断点击来源
        """
        send = self.land.sender()
        self.chess = send.text()
        self.check()

    def check(self, sign=0):
        """
        检查移动条件
        :param sign: 0->人类棋子; 1->高山
        """
        site = None
        state = None
        for i in range(len(self.land.cache)):
            if self.land.cache[i].text() == self.chess:
                site = i
                # 判断禁止地形
                if self.land.cache[i] in self.disable:
                    site = None
        # 安全检查通过，允许进军
        if site is not None:
            # 检查为人类棋子
            if sign == 0:
                for old_site in self.player.chess_map[self.player.round_now]:
                    if site == old_site:
                        state = 0
                self.march(site, state)
            # 检查为高山地形/导入初始军队地形
            if sign == 1:
                self.flag(self.land.cache[site], 'green')
            # 军队初始布局
            # 红方
            if sign == 2:
                self.flag(self.land.cache[site], 'red')
                self.player.chess_map[0].append(site)
            # 蓝方
            if sign == 3:
                self.flag(self.land.cache[site], 'blue')
                self.player.chess_map[1].append(site)
            # 禁止重复进入地形
            # self.disable.append(self.land.cache[site])
    def march(self, site, state):
        """
        棋子移动
        :param site: 点击位置
        :param state: 判断染色颜色，被点击的棋子变成白色，移动到新地方,0为消除点击棋子
        """
        # 保证交替下棋
        color = self.player.flag[self.player.id[self.player.round_now]]
        # 消除棋子并在下一步生成棋子，达到移动效果
        self.player.chess_map[self.player.round_now].append(site)
        if state == 0:
            color = 'white'
        self.flag(self.land.cache[site], color)
        self.player.player_round()

    def flag(self, chess, color):
        """
        棋子染色
        :param chess: 要染色的棋子
        :param color: 染后的颜色
        """
        chess.setStyleSheet("color : rgb(0,0,0,0);\n"
                            "background-color : {}".format(color))

class Player():
    """
    玩家信息
    """
    # 储存累计回合数
    round = 0
    round_now = None

    def __init__(self, player_number):
        # 储存身分组信息
        self.id = None
        self.flag = ['red', 'blue', 'yellow', 'black']
        self.chess_map = []
        self.player_chess(player_number)
        self.player_number = player_number
        self.player_round()

    def player_chess(self, player_number):
        """
        玩家的棋子信息
        """
        id = []
        for i in range(player_number):
            id.append(i)
            # 创建储存玩家拥有棋子的位置
            self.chess_map = [[]
                              for x in range(player_number)]
        self.id = id

    def player_round(self):
        """判断当前回合"""
        # 当前回合记录,0为红选红，1为红选白，2为蓝选蓝，3为蓝选白
        self.round_now = self.round % (self.player_number * 2)
        # 保证后续接口参数一致性，把四种类型变成玩家两种类型
        if self.round_now < 2:
            self.round_now = 0
        else:
            self.round_now = 1
        self.round += 1


class MapInit(SetMap):
    def __init__(self):
        """
        地图初始化
        """
        super(MapInit, self).__init__()

    def extend_map(self):
        """
        扩展地图
        """
        pass

    def define_terrain(self):
        """
        随机位置生成一座高山
        """
        self.chess_name = str(
            (random.randint(0, self.size_x - 1), random.randint(0, self.size_y - 1)))
        self.army_init()
    def army_init(self, mode=0):
        """
        军队部署初始化
        :param mode 初始军队布局样式
        """
        if mode == 0:
            self.chess_layout_1 = [(3, 0), (4, 1), (3, 1), (2, 0), (4, 2)]
            # 对称生成棋子
            self.chess_layout_2 = [(y, x) for (x, y) in self.chess_layout_1]
        self.chess_layout_1 = map(str, self.chess_layout_1)
        self.chess_layout_2 = map(str, self.chess_layout_2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Game()
    w.land.show()
    app.exec()
