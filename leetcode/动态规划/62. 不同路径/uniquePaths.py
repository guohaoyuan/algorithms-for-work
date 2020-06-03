# -*- coding : utf-8 -*-

class Solution(object):
    def uniquePaths(self, m, n):
        """
        动态规划：
        动态转移方程：dp[i, j] = dp[i - 1, j] + dp[i, j - 1]
        初始状态：
        dp[0, j] = 1
        dp[i, 0] = 1
        时间复杂度：nm，遍历整个二维数组
        空间复杂度：mn，建立一个新的二维数组存储结果
        :param m:
        :param n:
        :return:
        """
        # 1. 特殊情况：mn均为零
        if n == 0 or m == 0:
            return 0

        # 2. 初始化初始状态
        # 此时已经初始化第一行第一列的初始状态
        dp = [[1 for _ in range(n)] for _ in range(m)]

        # 3. 算法流程
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]

    def uniquePath2_v2(self, m, n):
        """
        为了优化空间复杂度，我们使用两个n长的数组分别表示上面一行pre，和本行cur
        动态转移方程cur[j] = cur[j-1] (已经更新，是本层的值)+ pre[j]\
        空间复杂度为2n
        :param m:
        :param n:
        :return:
        """
        # 1. 特殊情况：
        if m == 0 or n == 0:
            return 0

        # 2. 初始化两个行向量
        pre = [1 for _ in range(n)]
        cur = [1 for _ in range(n)]

        # 3. 算法流程
        for i in range(1, m):
            for j in range(1, n):
                cur[j] = cur[j - 1] + pre[j]
                # 小细节，我们这个过程需要更新pre
                pre = cur[:]    # 做一个浅拷贝
        return cur[-1]

    def uniquePaths_v3(self, m, n):
        """
        我们将pre和cur进行融合，
        动态转移方程：cur[j] = cur[j - 1] (表示已经更新过的本行) + cur[j] （表示未更新的上一行）
        空间复杂度为n
        :param m:
        :param n:
        :return:
        """
        # 1. 特殊情况
        if m == 0 or n == 0:
            return 0

        # 2. 初始化一个行向量
        cur = [1 for _ in range(n)]

        # 3. 算法流程
        for i in range(1, m):
            for j in range(1, n):
                cur[j] = cur[j] + cur[j - 1]
        return cur[-1]

if __name__ == '__main__':
    m1 = 3
    n1 = 2

    m2 = 7
    n2 = 3

    solution = Solution()
    print(solution.uniquePaths(m1, n1))
    print(solution.uniquePaths(m2, n2))
    print("===========================")
    print(solution.uniquePath2_v2(m1, n1))
    print(solution.uniquePath2_v2(m2, n2))
    print("===========================")
    print(solution.uniquePaths_v3(m1, n1))
    print(solution.uniquePaths_v3(m2, n2))