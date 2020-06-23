"""
主进程死了,子进程也死
"""
import multiprocessing
import time


def work1():
    for i in range(10):
        print("----work1----")
        time.sleep(1)


if __name__ == "__main__":
    process_obj = multiprocessing.Process(target=work1)
    process_obj.daemon = True
    process_obj.start()
    time.sleep(2)
    print("Game Over!")
    # 终止子进程的执行, 并非守护进程,而是调用命令杀死进程
    process_obj.terminate()
    exit()