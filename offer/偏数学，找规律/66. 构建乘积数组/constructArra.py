# -*- coding : utf-8 -*-

class Solution:
    def constructArr(self, a):
        """

        :param a: list
        :return: list
        """

        # 1. 初始化临时变量tmp，和返回结果数组b
        tmp = 1
        n = len(a)
        b = [1 for _ in range(n)]

        # 2. 计算左下角
        for i in range(1, n):
            b[i] = b[i - 1] * a[i - 1]

        for i in range(n - 2, -1, -1):
            tmp = tmp * a[i + 1]
            b[i] = b[i] * tmp

        return b

if __name__ == "__main__":
    a1 = [1,2,3,4,5]
    solution = Solution()
    print(solution.constructArr(a1))