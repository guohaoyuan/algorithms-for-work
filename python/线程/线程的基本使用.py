"""
如何创建线程
1. 导入threading
2. 使用threading.Thread()创建对象(子线程对象)
    threading.Thread(target=函数名)
3. 启动子线程对象,
    线程对象.start()
"""
import time
import threading


# 定义一个计时函数
def cal_time(func):
    def inner(*args):
        start = time.time()
        func(*args)
        end = time.time()
        print("执行 %d" % (start - end) * 1000)
    return inner


def apologize():
    print("老婆我错了!")
    time.sleep(1)


# @cal_time
def main():
    for i in range(5):
        threading_obj = threading.Thread(target=apologize)
        threading_obj.start()
    print("Xxx")


if __name__ == "__main__":
    # for i in range(5):
    #     threading_obj = threading.Thread(target=apologize)
    #     threading_obj.start()
    main()