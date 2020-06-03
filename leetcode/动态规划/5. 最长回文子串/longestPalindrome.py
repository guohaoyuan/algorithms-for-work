# -*- coding : utf-8 -*-

class Solution(object):
    def longestPalindrome(self, s):
        """
        首先想到暴力：两重循环，
        第一重，从头到尾遍历字符串，i
            第二重，从头到尾取j属于[0, i],
                    看[i, j]是否为回文
        时间复杂度：n**3

        所以我们继续考虑，引入动态规划，空间换时间，这是从中间往外扩散过程
        状态转移方程dp[i][j] = dp[i+1][j-1]   if s[i] == s[j] and (j-1)-(i+1) + 1>= 2
                              True          if s[i] == s[j] and j-1 - (i+1)  + 1< 2 表明字符串长度不足2,为1
                              False         if s[i] != s[j] 表明就不是字符串
        考虑初始状态：自下而上，初始状态为字符串长度==1,dp[i][i] = True

        整体上看，是一个缩小的过程
        :param s:
        :return:
        """
        # 1. 特殊情况： 字符串为空
        if not s:
            return ""

        # 2. 初始状态
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        max_len = 1
        res = s[0]

        for i in range(n):
            dp[i][i] = True


        # 3. 算法流程
        for j in range(1, n):
            for i in range(j):
                if s[i] == s[j]:
                    if (j - 1) - (i + 1) + 1 >= 2:
                        dp[i][j] = dp[i+1][j-1]
                        # 不用担心j到i长度不足2,此处做判断，之所以出现长度不足2,是因第二重循环[0,i]
                    else:
                        dp[i][j] = True
                else:
                    dp[i][j] = False


                # 在两重迭代过程中，更新最长回文的长度和起始位置

                if dp[i][j]:    # 必须当前为回文的情况下才能，更新最长长度和起始位置
                    if j - i + 1 > max_len:
                        max_len = j - i + 1
                        start_index = i
                        res = s[start_index : start_index + max_len]

        return res
    """
    时间复杂度：n**2，两重循环
    空间复杂度：n**2，有一个二维数组
    """

    def longestPalindrome_v2(self, s):
        """
        对于上面的空间复杂度不满意，优化空间复杂度
        使用中心扩散法：
        1. 特殊情况
        2. 初始化 最大长度 1 存放结果的res = s[0],这个有用，回文只能为1的时候
        3. 算法流程：先创建中心扩散的函数，不越界且相等，就扩
        遍历数组，分别按照奇数和偶数进行扩散，得到对应回文和长度
        比较两长度来判断，到低是奇数还是偶数
        4. 返回结果

        整体上看是一个扩大过程
        :param s:
        :return:
        """
        # 1. 特殊情况
        if not s:
            return ''

        # 2. 初始化
        res = s[0]
        max_len = 1

        # 3. 算法流程
        def center(i, j):
            """

            :param i: 传入左边索引
            :param j: 传入右边索引（目的是为了分奇数偶数两种情况）
            :return: 返回回文和对应长度
            """
            while 0 <= i and j < len(s) and s[i] == s[j]:  # 字符串相等，且左右边界不越界
                i -= 1
                j += 1
            # 越界后才返回，此时已经越界或者不相等
            return s[i + 1: j], j - i - 1

        # 遍历字符串，挨个字符进行中心扩散
        for i in range(len(s)):
            # 偶数
            odd_str, odd_len = center(i, i + 1)
            # 奇数
            even_str, even_len = center(i, i)

            # 比较两种情况的大小
            if even_len > odd_len and even_len > max_len:
                max_len = even_len
                res = even_str
            elif even_len < odd_len and odd_len > max_len:
                max_len = odd_len
                res = odd_str
        return res
    """
    时间复杂度：n**2
    空间复杂度：1
    """




if __name__ == '__main__':
    test1 = 'babad'
    test2 = 'c'
    solution = Solution()
    print(solution.longestPalindrome(test1))
    print(solution.longestPalindrome(test2))
    print("===============================")
    print(solution.longestPalindrome_v2(test1))
    print(solution.longestPalindrome_v2(test2))