"""
获取进程的名称 multiprocessing.current_process()

获取进程的编号pid,两种方法
1. multiprocessing.current_process().pid
2. 利用os模块获取, os.getpid()


获取子进程的父id
os.getppid()
"""
import time
import multiprocessing
import os


def work1():
    for i in range(10):
        print("work1...", i, multiprocessing.current_process(), multiprocessing.current_process().pid)
        print("子进程的父id", os.getppid())
        time.sleep(1)


if __name__ == "__main__":
    print(multiprocessing.current_process())
    print(multiprocessing.current_process().pid)
    print(os.getpid())
    # name参数指定子进程名字
    process_obj = multiprocessing.Process(target=work1, name="P1")

    process_obj.start()

    print("XXX")