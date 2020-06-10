# -*- coding : utf-8 -*-

class Solution:

    def hamming(self, n):
        # 1. 特殊情况数字

        # 2. 初始化列表res存储二进制
        res = []

        # 3. 算法流程n&1,然后n右移位
        while n:
            if n & 1 == 1:
                res.append(1)
            else:
                res.append(0)
            n = n >> 1
        return res[::-1]


if __name__ == "__main__":
    test1 = 10
    solution = Solution()
    print(solution.hamming(test1))