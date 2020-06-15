# -*- coding : utf-8 -*-

class MusicPlayer(object):
    # 1. 创建类属性，用于记录创建对象的引用
    instance = False

    def __new__(cls, *args, **kwargs):
        # 2. 首先判断类属性是否为空，如果为空，则调用父类的__new__方法
        if cls.instance is None:
            # 2. 为第一个对象分配空间
            cls.instance = super().__new__(cls)

        # 3. 返回类属性的引用
        return cls.instance

if __name__ == "__main__":
    player1 = MusicPlayer()
    print(id(player1))
    player2 = MusicPlayer()
    print(id(player2))