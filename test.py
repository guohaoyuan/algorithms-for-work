# str = ["a", "b", "c", "d"]
#
# for ch in str:
#     if ch == "c":
#         print("hello")
#         break
#     print("ch" + ch)
# else:
#     print("not found")
# print("world")

# print(list(map(str, [10, 20, 30])))

# def func():
#     x = 1/0
#     print("func")
#
# try:
#     func()
#     print("try")
# except ZeroDivisionError as err:
#     print("excerpt")
# finally:
#     print("finally")

# import numpy as np
#
# arr = np.arange(12).reshape(3, 4)
# print(arr[0:2])
# import time
# import threading
# def run(n):
#     print("task")
#     time.sleep(1)
#     print("A")
#     time.sleep(1)
#     print("B")
#     time.sleep(1)
#     print("C")
#
# if __name__ == '__main__':
#     t = threading.Thread(target=run, args=("t1", ))
#     t.setDaemon(True)
#     t.start()
#     t.join()
#     print("end")

# def a(v):
#     v = v +3
#
# c = 1
# a(c)
# # print(c)
# class P(object):
#     pass
#
# class F(object):
#     pass
#
# class C(P):
#     pass
#
# c = C()
# p = F()
# print(isinstance(c, p))
# # print(isinstance(p, c))

# import sys
#
#
# for i in range(2):
#     line = sys.stdin.readline()
#     print(type(line))

# a = input()
# import time
#
#
# def outer(func):
#     def inner(*args):
#         start = time.time()
#         func(*args)
#         end = time.time()
#         print(end - start)
#     return inner

#
# a = [1, 2, 3, 4]
#
# b = a[1:3]
# print(a is b)

# nums = int(input())
# points = []
# for i in range(0, nums):
#     read_list = ''.join(map(str, input().split()))
#     print(read_list)
#     # read_list = [int(i) for i in input().split()]
#     points.append((read_list[0], read_list[1]))
    # print(points)

# def a():
#     try:
#         return 1
#     finally:
#         return 2
# k = a()
# print(k)




def longestCommonSubsequence(text1: str, text2: str) -> int:
    if not text1 or not text1:
        return 0

    m = len(text1)
    n = len(text2)
    # 因为有空字串
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            #  因为ddp table比字符串多一位，dp table中的i,j在字符串中对应索引是i-1,j-1
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(max(dp[i-1][j], dp[i][j-1]), dp[i-1][j-1])
    return dp[-1][-1]

dna_len = int(input())
dna_nums = []
for i in range(3):
    if i == 0:
        continue
    dna_nums.append(''.join(map(str, input().split())))
dna1 = dna_nums[0]
dna2 = dna_nums[1]

text1 = dna1
text2 = dna2

dna_longest = longestCommonSubsequence(text1, text2)

similar = dna_longest / dna_len
similar = round(similar, 2)
hun = "Yes" if similar <= 0.5 else "No"
output = str(similar) + ' ' + hun
print(output)