# -*- coding : utf-8 -*-

class Solution:
    def twoSum(self, n):
        """

        :param n: int
        :return: list
        """
        # 1. 初始状态：一个骰子的点数概率
        pre = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]

        # 2. 动态转移
        for i in range(2, n + 1):
            # 表示有几个骰子
            # 初始化临时数组
            tmp = [0 for _ in range(5 * i + 1)]

            # 遍历前一个数组
            for x in range(len(pre)):
                # 遍历只有一个骰子的数组
                for y in range(6):
                    # 根据动态转移方程，更新临时数组
                    tmp[x + y] += pre[x] * (1/6)
            # 将临时数组给pre,更新pre
            pre = tmp
        return pre

if __name__ == "__main__":
    n1 = 1
    n2 = 2
    solution = Solution()
    print(solution.twoSum(n1))
    print(solution.twoSum(n2))