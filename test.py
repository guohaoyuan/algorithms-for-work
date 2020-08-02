# str = ["a", "b", "c", "d"]
#
# for ch in str:
#     if ch == "c":
#         print("hello")
#         break
#     print("ch" + ch)
# else:
#     print("not found")
# print("world")

# print(list(map(str, [10, 20, 30])))

# def func():
#     x = 1/0
#     print("func")
#
# try:
#     func()
#     print("try")
# except ZeroDivisionError as err:
#     print("excerpt")
# finally:
#     print("finally")

# import numpy as np
#
# arr = np.arange(12).reshape(3, 4)
# print(arr[0:2])
# import time
# import threading
# def run(n):
#     print("task")
#     time.sleep(1)
#     print("A")
#     time.sleep(1)
#     print("B")
#     time.sleep(1)
#     print("C")
#
# if __name__ == '__main__':
#     t = threading.Thread(target=run, args=("t1", ))
#     t.setDaemon(True)
#     t.start()
#     t.join()
#     print("end")

# def a(v):
#     v = v +3
#
# c = 1
# a(c)
# # print(c)
# class P(object):
#     pass
#
# class F(object):
#     pass
#
# class C(P):
#     pass
#
# c = C()
# p = F()
# print(isinstance(c, p))
# # print(isinstance(p, c))

# import sys
#
#
# for i in range(2):
#     line = sys.stdin.readline()
#     print(type(line))

# a = input()
# import time
#
#
# def outer(func):
#     def inner(*args):
#         start = time.time()
#         func(*args)
#         end = time.time()
#         print(end - start)
#     return inner

#
# a = [1, 2, 3, 4]
#
# b = a[1:3]
# print(a is b)

class Solution:
    # 1 .
    instance = False

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super().__new__(cls)
        return cls.instance