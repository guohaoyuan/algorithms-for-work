# -*- coding : utf-8 -*-

class Solution:
    def add(self, a, b):
        """

        :param a: int
        :param b: int
        :return: int
        """
        # 1. 初始化a ,b
        x = 0xffffffff
        # 取补码
        a = a & x
        b = b & x

        # 2. 循环进位和非进位操作
        while b != 0:   # 进位操作为0,结束
            a, b = a ^ b, (a & b) << 1 & x

        return a if a <= 0x7fffffff else ~(a ^ x)



if __name__ == "__main__":
    a1 = 1
    b1 = 1
    solution = Solution()
    print(solution.add(a1, b1))