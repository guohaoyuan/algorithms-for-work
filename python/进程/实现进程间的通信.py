"""
进程间通信
思路:
1. 准备两个进程
2. 准备一个队列,
3. 一个进程向队列中写入数据,然后队列传递到另一个进程
4. 一个进程读取数据

进程对象.join() 先让进程执行完成,在取其动读的进程；否则会出现两进程同时进行
"""

import time
import multiprocessing


# 1. 写入数据到队列
# 需要传入参数一个队列
def write_queue(queue):
    for i in range(10):
        if queue.full():
            print("队列已满!")
            break
        # 插值
        queue.put(i)
        print("成功加入元素 %d" % i)
        time.sleep(0.5)


# 2. 从队列读取数据
def read_queue(queue):
    for i in range(10):
        if queue.qsize() == 0:
            print("队列已空!")
            break
        # 取值
        value = queue.get()
        print("成功读取元素 %d" % value)
        # time.sleep(0.5)

if __name__ == "__main__":
    # 创建队列
    queue = multiprocessing.Queue(5)


    # 创建两个进程,一个读数据. 一个写数据
    write_queue1 = multiprocessing.Process(target=write_queue, args=(queue, ))
    read_queue1 = multiprocessing.Process(target=read_queue, args=(queue, ))
    print(write_queue1.enumerate())

    # 让读数据进程执行完毕,在执行读取进程
    write_queue1.start()
    write_queue1.join()

    read_queue1.start()