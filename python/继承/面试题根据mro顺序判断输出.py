# class A(object):
#     def __init__(self):
#         print("A")
#
#
# class B(A):
#     def __init__(self):
#         super().__init__()
#         print("B")
#
#
# class C(A):
#     def __init__(self):
#         super().__init__()
#         print("C")
#
#
# class D(B, C):
#     def __init__(self):
#         super().__init__()
#         print("D")
#
#
# d = D()
# print(D.__mro__)
"""
A
C
B
D
"""


class A(object):
    def __init__(self):
        print("A")


class B(A):
    def __init__(self):
        # super().__init__()
        A.__init__(self)
        print("B")


class C(A):
    def __init__(self):
        # super().__init__()
        A.__init__(self)
        print("C")


class D(B, C):
    def __init__(self):
        super().__init__()
        print("D")


d = D()
print(D.__mro__)
"""
A
B
D
"""