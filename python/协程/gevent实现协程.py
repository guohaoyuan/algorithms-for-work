"""
gevent自动识别程序中的耗时操作,在耗时操作时候自动切换到其他任务

1. 导入模块

2. 指派任务
"""

import time
import gevent


def work1():
    while True:
        print("work1 正在执行.....")
        # yield
        # time.sleep(0.5)
        # gevent只能识别gevent.sleep
        # 或者给程序打补丁
        # 打补丁: 在不修改程序源代码的情况下,为程序增加新的功能
        # 如何打补丁:
        #           1. 导入猴子补丁monkey, from gevent import monkey
        #           2. 破解 monkey.patch_all()
        gevent.sleep(0.5)


def work2():
    while True:
        print("work2 正在执行...................")
        # yield
        # time.sleep(0.5)
        gevent.sleep(0.5)


if __name__ == '__main__':
    # 指派任务,
    # gevent.spawn(函数名, 参数...)
    g1 = gevent.spawn(work1)
    g2 = gevent.spawn(work2)

    g1.join()
    g2.join()