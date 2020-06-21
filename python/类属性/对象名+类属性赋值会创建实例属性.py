class Tool(object):
    count = 0

    def __init__(self, name):
        self.name = name

        Tool.count += 1

tool1 = Tool("斧头")
tool2 = Tool("小刀")
tool3 = Tool("水桶")

tool3.count = 99
print("水桶对象 %s" % tool3.count)
print("水桶对象赋值语句 %s" % Tool.count)