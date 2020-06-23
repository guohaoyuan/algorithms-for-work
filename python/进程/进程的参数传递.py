import multiprocessing
import time


def work1(a, b, c):
    print("传入参数 a = %d, b = %d, c = %d" % (a, b, c))
    for i in range(10):
        print("进程work1....")
        time.sleep(1)


if __name__ == "__main__":
    # multiprocessing_obj = multiprocessing.Process(target=work1, args=(1, 2, 3))
    # multiprocessing_obj = multiprocessing.Process(target=work1, kwargs={"a": 1, "b": 2, "c": 3})
    multiprocessing_obj = multiprocessing.Process(target=work1, args=(1, ), kwargs={"c": 2, "b": 3})
    multiprocessing_obj.start()