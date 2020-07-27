"""
1. 定义状态
        dp[i][j]表示字符串str1[:i-1] 和 字符串str2[:j-1]他们的LCS长度为dp[i][j]
        dp table 0行0列表示空字符”“

2. 转移方程：重在选择
        dp[i][j] =
        如果两个str1[i-1] == str2[j-1]（表示当期字符相等，则LCS长度+1），
                                dp[i][j] = dp[i-1][j-1] + 1
        如果两个str1[i-1] != str2[j-1]（表示有可能一个字符不在lcs中，也可能两个字符都不在lcs中）
                                dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

3. base case 0行0列均为0

note: dp table 为m+1 * n+1
      str1       m
      str2             n
所以dp[i][j]对应str1[i-1] str2[j-1]是否匹配
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
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


"""
优化空间复杂度

我们发现，用不着整个dptable，主要用到当前行和前一行

"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text1:
            return 0

        m = len(text1)
        n = len(text2)
        # 因为有空字串
        # dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        dp = [0 for _ in range(n + 1)]

        for i in range(1, m + 1):  # 行
            tmp = dp[:]  # 存储上一行
            for j in range(1, n + 1):
                #  因为ddp table比字符串多一位，dp table中的i,j在字符串中对应索引是i-1,j-1
                if text1[i - 1] == text2[j - 1]:
                    # dp[i][j] = dp[i-1][j-1] + 1
                    dp[j] = tmp[j - 1] + 1
                else:
                    # dp[i][j] = max(max(dp[i-1][j], dp[i][j-1]), dp[i-1][j-1])
                    dp[j] = max(dp[j], dp[j - 1])   # 实际上是tmp[j], dp[j-1]中最大的，但是tmp[j]还没来得及被覆盖，所以直接使用
        return dp[-1]


"""
优化空间复杂度

我们只需要一个变量存储tmp[j-1]
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text1:
            return 0

        m = len(text1)
        n = len(text2)
        # 因为有空字串
        # dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        dp = [0 for _ in range(n + 1)]

        for i in range(1, m + 1):  # 行
            # tmp = dp[:]    # 存储上一行
            last = 0
            for j in range(1, n + 1):
                tmp = dp[j]  # 每次运行完tmp就是上一行的dp[j],比如tmp = dp[j = 1] 下次迭代tmp = dp[j = 2] 而此时last = dp[j = 1]
                #  因为ddp table比字符串多一位，dp table中的i,j在字符串中对应索引是i-1,j-1
                if text1[i - 1] == text2[j - 1]:
                    # dp[i][j] = dp[i-1][j-1] + 1
                    dp[j] = last + 1
                else:
                    # dp[i][j] = max(max(dp[i-1][j], dp[i][j-1]), dp[i-1][j-1])
                    dp[j] = max(dp[j], dp[j - 1])
                # 更新
                last = tmp

        return dp[-1]