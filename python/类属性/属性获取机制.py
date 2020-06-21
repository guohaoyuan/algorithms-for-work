class Tool(object):

    count = 0

    def __init__(self, name):
        self.name = name
        Tool.count += 1

tool1 = Tool("小刀")
tool2 = Tool("斧头")
tool3 = Tool("剪刀")

print(tool3.count)