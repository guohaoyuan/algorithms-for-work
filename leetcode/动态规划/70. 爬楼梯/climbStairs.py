# -*- coding : utf-8 -*-

class Solution(object):
    def climbStairs(self, n):
        """
        动态规划：类似斐波那契数列
        动态转移方程：dp[i] = dp[i - 1] + dp[i-2]
        初始状态：可以看出要两个状态dp_one = 1 dp_two = 2,即第一节台阶和第二节台阶
        :param n:
        :return:
        """
        # 1. 特殊情况：n为0
        if n < 3:
            return n

        # 2. 初始化动态转移初始状态
        dp_one = 1
        dp_two = 2

        # 3. 算法流程
        for i in range(2, n):
            tmp = dp_one + dp_two
            dp_one = dp_two
            dp_two = tmp
        return dp_two

if __name__ == '__main__':
    test1 = 2
    test2 = 5
    solution = Solution()
    print(solution.climbStairs(test1))
    print(solution.climbStairs(test2))
    """
    时间复杂度：n，
    空间复杂度：1
    """