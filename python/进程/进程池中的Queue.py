"""
进程池中的进程间通信

进程池中的队列创建 不同与之前
multiprocessing.Manager().Queue(数目)


1. 写数据到队列,读数据
2. 创建进程池
3. 创建进程池中的队列
4. 使用进程池执行任务
    4.1 同步方式
    4.2 异步方式
        apply_async()返回值ApplyResult对象,该对象有一个wait()方法, 让当前进程执行完毕,后续进程才执行.类似join
"""

# 1. 导入模块
import time
import multiprocessing


# 2. 创建写入函数 和读取函数
def write_pool(queue):
    for i in range(10):
        if queue.full():
            print("进程池已经满了!")
            break
        queue.put(i)
        print("插入元素 %d" % i)
        time.sleep(0.5)


def read_pool(queue):
    for i in range(10):
        if queue.qsize() == 0:
            print("进程池已经空了!")
            break
        value = queue.get()
        print("读取元素 %d" % value)
        time.sleep(0.5)


if __name__ == '__main__':
    # 3. 创建进程池
    pool = multiprocessing.Pool(3)

    # 4. 创建进程池的信息队列
    queue = multiprocessing.Manager().Queue(3)

    # 同步和异步操作
    # pool.apply(write_pool, (queue, ))
    # pool.apply(read_pool, (queue, ))

    # 异步操作需要先创建异步操作对象,利用对象中的wait()方法
    write_obj = pool.apply_async(write_pool, (queue, ))
    # 让写入操作执行完,在执行后续操作
    write_obj.wait()
    pool.apply_async(read_pool, (queue, ))
    # 不再接受新任务
    pool.close()
    # 主进程等待进程池结束
    pool.join()