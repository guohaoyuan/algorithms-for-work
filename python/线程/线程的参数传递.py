import threading
import time


"""
在线程中传递参数有三种方法, 
1. 使用元组传递threading.Thread(target=xx, args=(参数1, 参数2,...))
2. 使用字典传递threading.Thread(target=xx, kwargs={})
3. 同时使用元组和字典传参
"""


def sing(a, b, c):
    print("参数 a %d, b %s, c %s" % (a, b, c))
    for i in range(5):
        print("singing")
        time.sleep(0.5)


def dance(a, b, c):
    print("参数 a %d, b %s, c %s" % (a, b, c))
    for i in range(5):
        print("dancing")
        time.sleep(0.5)


if __name__ == "__main__":
    threading_obj1 = threading.Thread(target=sing, args=(1, 2, 3))
    threading_obj2 = threading.Thread(target=dance, kwargs={"a": 1, "b": 2, "c": 3})
    threading_obj1.start()
    threading_obj2.start()