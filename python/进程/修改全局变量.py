"""
在函数中可以直接访问全局变量, 但是不能改变自身
如果需要修改,需要使用global关键字


进程之间全局变量的不共享
子进程互相独立, 都是把资源复制了一份

线程之间资源共享,全局变量共享
"""

import threading
import multiprocessing
import time


g_num = 0


def work1():
    global g_num
    for i in range(10):
        g_num = g_num + 1
    print("------work1------", g_num)


def work2():
    print("------work2------", g_num)


if __name__ == "__main__":
    # work1_multiprocessing = multiprocessing.Process(target=work1)
    # work2_multiprocessing = multiprocessing.Process(target=work2)
    # work1_multiprocessing.start()
    # work2_multiprocessing.start()
    # print("主进程g_num = ", g_num)


    # work1()
    # work2()

    threading_work1 = threading.Thread(target=work1)
    threading_work2 = threading.Thread(target=work2)
    threading_work1.start()
    threading_work2.start()