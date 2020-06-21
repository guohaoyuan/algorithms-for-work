"""开发一个工具类, 创建一个类属性count 进行计数多少个实例"""

class Tool(object):
    # 创建类属性,用于统计工具对象的数目
    count = 0
    bag = "工具包"

    def __init__(self, name):
        self.name = name
        Tool.count += 1
        print("工具包有%d个工具" % Tool.count)
        print(bag)
# 1. 初始化实例
futou = Tool('斧头')
jiandao = Tool('剪刀')
xiaodao = Tool('笑道')

