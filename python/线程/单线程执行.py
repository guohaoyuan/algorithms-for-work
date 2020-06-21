import time


def apologize():
    print("老婆我错了!")
    time.sleep(1)


# 单线程方式
if __name__ == "__main__":
    for i in range(5):
        apologize()