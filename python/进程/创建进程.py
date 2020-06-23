"""
1. 导入模块
2. 创建进程对象
3. 启动进程对象
"""
import time
import multiprocessing


def work1():
    for i in range(10):
        print("work1...")
        time.sleep(1)


if __name__ == "__main__":
    multiprocessing_obj = multiprocessing.Process(target=work1)
    multiprocessing_obj.start()

    print("xxx")