"""
1. 创建生成器
2. 生成器对象实例化
3. 执行生成器next
"""
import time


def work1():
    while True:
        print("work1 正在执行.....")
        yield
        time.sleep(0.5)

def work2():
    while True:
        print("work2 正在执行...................")
        yield
        time.sleep(0.5)


if __name__ == '__main__':
    w1 = work1()
    w2 = work2()

    while True:
        next(w1)
        next(w2)