#!/usr/bin/python
#-- coding:utf8 --
import threading
import time


def sing():
    for i in range(5):
        print("singing...", threading.current_thread())     # 获取线程的名称
        time.sleep(1)


def dancing():
    for i in range(5):
        print("dancing...")
        time.sleep(1)


if __name__ == "__main__":

    threading_sing = threading.Thread(target=sing)
    threading_dance = threading.Thread(target=dancing)

    threading_sing.start()
    threading_dance.start()
    while True:
        threading_list = threading.enumerate()      # 当前活跃的线程列表
        print("当前线程数目", len(threading_list))
        if len(threading_list) <= 1:
            break
        time.sleep(1)