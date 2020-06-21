"""
创建类属性 记录历史最高分
创建类方法 输出历史最高分
创建静态方法 提供帮助信息
创建实例方法 开始游戏
"""

class Game(object):

    top_score = 0

    def __init__(self, player_name):
        self.player_name = player_name

    @classmethod
    def print_top_score(cls):
        print("历史最高分为 %d " % Game.top_score)
        # cls.ex()
        # cls.helper()

    @staticmethod
    def helper():
        print("僵尸没了")

    def start_game(self):
        print("%s 开始游戏" % self.player_name)

    # @classmethod
    # def ex(cls):
    #     print("aa")
#  调用类方法
Game.print_top_score()

# 调用静态方法
Game.helper()

# 调用普通方法
player = Game("小明")
player.start_game()

"""
"""