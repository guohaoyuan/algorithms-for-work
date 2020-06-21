# -*- coding : utf-8 -*-
### 动机:在读写操作报错时,无法及时释放内存 ###
# f = open('write.txt', 'r')
# f.write("wwww") # ioerror: No such file or directory: 'write.txt'
# f.close()

### 尝试try/finally语句解决 ###
try:
    f = open('write.txt', 'r')
    f.write('wwww')
except IOError as Exception1:
    print("ioerror ", Exception1)
finally:        # 无论是否报错
    f.close()   # 这里是必须要执行的
