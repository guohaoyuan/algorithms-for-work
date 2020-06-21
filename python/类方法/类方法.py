class Tool(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Tool.count += 1
        print("创建一个新工具 %s" % self.name)

    @classmethod
    def tool_count(cls):
        print("工具对象的总数 %d" % Tool.count)


tool1 = Tool("斧头")
Tool.tool_count()