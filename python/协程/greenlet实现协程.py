"""
1. 创建函数, 函数中使用swich()

2. 用greenlet创建协程

3. 使用swich()调用协程对象

"""
import time
from greenlet import greenlet


def work1():
    while True:
        print("work1 正在执行...")
        time.sleep(0.5)
        g2.switch()


def work2():
    while True:
        print("work2 正在执行............")
        time.sleep(0.5)
        g1.switch()


if __name__ == '__main__':
    g1 = greenlet(work1)
    g2 = greenlet(work2)

    g1.switch()