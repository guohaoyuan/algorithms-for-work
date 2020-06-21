"""
思路:
定义自己的函数,并使用装饰器
@contextmanager
def myopen(filename, mode):
    1. 进入上文
    2. yield
    3. 进入下文

调用函数myopen
with myopen(filename, mode) as f:
    读写操作
"""

from contextlib import contextmanager

@contextmanager
def myopen(filename, mode):
    f = open(filename, mode)
    yield f
    f.close()

with myopen("out.txt", 'r') as f:
    readlines = f.read()
    print(readlines)