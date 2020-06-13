# -*- coding : utf-8 -*-

class Solution:
    def nthUglyNumber(self, n):
        """

        :param n: int
        :return: int
        """
        # 1, 特殊情况：输入<0
        if n <= 0:
            return

        # 2. 初始化返回结果res数组，和三个维护数组下标
        index1 = 0
        index2 = 0
        index3 = 0
        res = [1 for _ in range(n)]     # 只存放丑数，且有序

        # 3. 算法流程维护res
        for i in range(1, n):
            res[i] = min(min(res[index1] * 2, res[index2] * 3), res[index3] * 5)

            # 更新对应下标
            if res[index1] * 2 == res[i]:
                index1 += 1
            if res[index2] * 3 == res[i]:
                index2 += 1
            if res[index3] * 5 == res[i]:
                index3 += 1
        return res[-1]

if __name__ == "__main__":
    n1 = 10
    n2 = 1
    solution = Solution()
    print(solution.nthUglyNumber(n1))
    print(solution.nthUglyNumber(n2))
    """
    时间复杂度：n
    空间复杂度：n
    """