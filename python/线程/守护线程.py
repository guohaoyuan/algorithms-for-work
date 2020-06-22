"""
1. 导包
2. 创建线程对象
3. 设置守护线程
4. 开始线程对象
"""

import threading
import time


def work1():
    for i in range(10):
        print("lalalala...")
        time.sleep(1)


if __name__ == "__main__":
    threading_work1 = threading.Thread(target=work1)
    threading_work1.setDaemon(True)  # 设置线程守护
    threading_work1.start()
    time.sleep(3)
    print("Game over")