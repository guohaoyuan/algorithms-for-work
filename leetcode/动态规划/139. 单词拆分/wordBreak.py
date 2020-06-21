# -*- coding : utf-8 -*-

class Solution:

    def wordBreak(self, s, wordDict):
        """

        :param s: 非空字符串
        :param wordDict: 非空单词列表
        :return: 布尔值
        """
        # 1. 特殊情况：字符串s为空，直接返回True
        if not s:
            return True

        # 2. 初始化状态数组，初始化为F，初始状态为T
        # 动态转移方程dp[i]表示字符串s的前i位，可以分割后的单词均在wordDict中
        n = len(s)
        dp = [False for _ in range(n + 1)]
        dp[0] = True

        # 3. 算法流程
        # 状态转移方程：dp[j]=True, if dp[i]=True and s[i : j + 1] in wordDict
        for i in range(n):  # 遍历字符串

            for j in range(i + 1, n + 1):   # 第二层遍历是为了填充n+1长的dp数组
                # 因为有两重循环，所以不能优化空间
                if dp[i] and s[i: j] in wordDict:
                    dp[j] = True
                # 否则就是False
        return dp[-1]
if __name__ == "__main__":
    s1 = "leetcode"
    wordDict1 = ["leet", "code"]
    s2 = "applepenapple"
    wordDict2 = ["apple", "pen"]
    s3 = "catsandog"
    wordDict3 = ["cats", "dog", "sand", "and", "cat"]
    solution = Solution()
    print(solution.wordBreak(s1, wordDict1))
    print(solution.wordBreak(s2, wordDict2))
    print(solution.wordBreak(s3, wordDict3))
    """
    时间复杂度：n^2,
    空间复杂度：n
    """