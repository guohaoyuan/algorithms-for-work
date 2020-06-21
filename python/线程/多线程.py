import threading
import time


def sing():
    for i in range(5):
        print("singing...")
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

    threading_list = threading.enumerate()
    print("当前线程数目", len(threading_list))