"""
1. 定义状态dp[i]表示前i个字符组成的字符串在worddict中
2. 定义转移方程
        如果dp[i]为True，且i到j所组成的字符也在wordDict中，
            dp[j] = True
3. base case dp[0] = True表示空字符串
"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(n):  # 第一层是遍历字符串s
            for j in range(i + 1, n+1):   # 第二层是截断一个字符串，并判断是否在worddict中
                if dp[i] and s[i:j] in wordDict:
                    dp[j] = True
        return dp[-1]