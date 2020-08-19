"""
这是鹅厂或者说是大厂的一道算法题。

首先这是一个动态规划
我们顺便普及以下动态规划和分治算法的联系
动态规划可以理解成一种分治思想，但是分治算法把原问题分解乘若干子问题，自上而下求解，合并子问题的解。比如归并排序。
动态规划处理的是有重叠子问题，且有最优子结构。自底向上，没有重复计算，从而提高效率。
理解什么是最优子结构：简单来说就是，保证了子问题取得最优解，就能使的最终问题取得最优解
理解什么是无后效性：当前结果不会受到后面阶段的影响。
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1:
            return len(word2)

        if not word2:
            return len(word1)

        dp = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]

        for i in range(len(word2) + 1):
            dp[0][i] = i

        for i in range(len(word1) + 1):
            dp[i][0] = i

        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j - 1], dp[i - 1][j]) + 1
                    # 插入      替换            删除
        return dp[-1][-1]