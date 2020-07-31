"""
要求尽可能的优化复杂度
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 1. 特殊情况：数组为空
        if not s:
            return ""

        # 2. 初始化
        max_len = 1
        res = s[0]
        n = len(s)

        # 定义中心扩散函数
        def center(s, i, j):
            while 0 <= i and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return s[i + 1: j], j - i - 1

        for i in range(n):
            odd_str, odd_len = center(s, i, i)
            even_str, even_len = center(s, i, i + 1)
            if odd_len > even_len and odd_len > max_len:
                max_len = odd_len
                res = odd_str
            elif even_len > odd_len and even_len > max_len:
                max_len = even_len
                res = even_str
        return res