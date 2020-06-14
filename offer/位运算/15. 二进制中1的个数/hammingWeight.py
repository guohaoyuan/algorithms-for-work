# -*- coding : utf-8 -*-

class Solution:
    def hammingWeight(self, n):
        """

        :param n: int
        :return: int
        """
        # 1.

        # 2. 初始化res
        res = 0

        # 3. 算法流程
        while n:
            res += 1
            n = (n - 1) & n
        return res

if __name__ == '__main__':
    n1 = 11
    n2 = 3
    solution = Solution()
    print(solution.hammingWeight(n1))
    print(solution.hammingWeight(n2))
    """
    时间复杂度：n，对于输入1的个数
    空间复杂度：1
    """