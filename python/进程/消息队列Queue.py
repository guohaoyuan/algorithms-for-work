"""
Queue 为了实现进程间的通信

创建队列,指定长度
.put() 表示插值
.get() 表示取值
"""


import multiprocessing


# 1. 创建队列
queue = multiprocessing.Queue(5)

# 2. 插值
queue.put(1)
queue.put("hello")
queue.put([1, 2, 3])
queue.put((1, 2, 3))
queue.put({"a": 1, "b": 2})

# .put()如果超过长度,会进入阻塞状态, 且程序不会结束, 默认等待队列先取出值,再放入新的值
# queue.put("ghy")

# .put_nowait() 不进入阻塞状态的差值,如果队列已经满了,报错
# queue.put_nowait("ghy")

# 3. 取值
value = queue.get()
print(value)
print("--"*20)

value = queue.get()
print(value)
print("--"*20)

value = queue.get()
print(value)
print("--"*20)

value = queue.get()
print(value)
print("--"*20)

value = queue.get()
print(value)
print("--"*20)

# 当队列已经为空,再次get()进入阻塞状态,等待放入新值到队列中, 然后取出


# get_nowait() 当队列已经空,不再等待,直接报错
# value = queue.get_nowait()
# print(value)
# print("--"*20)