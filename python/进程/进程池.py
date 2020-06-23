"""
同步
apply(函数名, 传递给函数的参数)


异步
apply_async(func[args[, kwds]])
需要做两点:
1) 必须进行关闭操作 pool.close() 表示不再接受新的任务
2) 主进程不再等待进程池执行结束在退出, 需要进程池pool.join() , 让主进程等待进程池执行结束后再退出


1. 创建一个函数,用于模拟文件拷贝

2. 创建一个进程池,长度为3,表示进程池中,最多创建三个进程

3. 用进程池同步方式拷贝文件

4. 用进程池异步方式拷贝文件
"""

# 1. 导入模块
import time
import multiprocessing


# 2. 创建函数
def copy_work():
    print("正在拷贝文件....", multiprocessing.current_process())
    time.sleep(0.5)



if __name__ == "__main__":
    # 3. 创建进程池
    pool = multiprocessing.Pool(3)
    for i in range(10):
        # 同步执行, 只需要下面一句
        # pool.apply(copy_work)
        #
        # 异步执行, 需要close  join
        pool.apply_async(copy_work)

    pool.close()
    pool.join()