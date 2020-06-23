
class MusicPlayer(object):
    # 1. 创建一个类属性，记录被创建对象的引用 ###
    instance = None

    # 1. 创建一个类属性，用于记录是否执行初始化操作
    init_flag = False

    def __new__(cls, *args, **kwargs):
        # 2. 首先判断类属性是否为空，如果为空调用父类new方法 ###
        if cls.instance is None:
            cls.instance = super().__new__(cls)

        # 3. 返回创建对象的引用 ###
        return cls.instance

    def __init__(self, *args, **kwargs):
        # 2. 判断类属性是否执行过初始化操作，如果执行过，直接返回
        if self.init_flag:
            return
        # 3. 如果没有执行过，执行初始化动作
        print("初始化播放器")

        # 4. 修改类属性的标记
        self.init_flag = True

if __name__ == "__main__":
    player1 = MusicPlayer()
    print(id(player1))
    player2 = MusicPlayer()
    print(id(player2))