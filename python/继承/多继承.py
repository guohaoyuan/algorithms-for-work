
"""多继承, super的动机, 如果使用父类名.父类方法, 会导致子类多次调用父类方法, 如果是打开文件,就会浪费资源."""


# class Parent(object):
#     def __init__(self, name):
#         self.name = name
#         print("Parent被调用")
#
#
# class Son1(Parent):
#     def __init__(self, name):
#         self.name = name
#         # 调用父类方法
#         Parent.__init__(self, name)
#         print("Son1被调用")
#
#
# class Son2(Parent):
#     def __init__(self, name):
#         self.name = name
#         # 调用父类方法
#         Parent.__init__(self, name)
#         print("Son2被调用")
#
#
# class GrandSon(Son1, Son2):
#     def __init__(self, name):
#         self.name = name
#         # 调用两个Son方法
#         Son1.__init__(self, name)
#         Son2.__init__(self, name)
#         print("GrandSon被调用")
#
#
# GrandSon("grandson")
"""
Parent被调用
Son1被调用
Parent被调用
Son2被调用
GrandSon被调用
"""


"""利用super来解决上面的问题"""


class Parent(object):
    def __init__(self, name):
        self.name = name
        print("Parent被调用")


class Son1(Parent):
    def __init__(self, name):
        self.name = name
        super().__init__(name)
        print("Son1被调用")


class Son2(Parent):
    def __init__(self, name):
        self.name = name
        super().__init__(name)
        print("Son2被调用")


class GrandSon(Son1, Son2):
    def __init__(self, name):
        self.name = name
        super().__init__(name)
        print("GrandSon被调用")


GrandSon("GHY")