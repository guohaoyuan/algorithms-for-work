# -*- coding : utf-8 -*-

class Solution:
    def reverseWords(self, s):
        # 1. 特殊情况，字符串为空，则返回空字符串
        if not s:
            return ""

        # 2. 初始化res，存放结果，双指针i j
        s = s.strip()   # 去除首位空格
        n = len(s)
        i, j = n - 1, n - 1
        res = []

        # 3. 算法流程：
        # 当i >= 0
        while i >= 0:
            while i >= 0 and s[i] != ' ':
                i -= 1
            # 一直到遇到空字符串
            res.append(s[i + 1: j + 1])

            # 找到下一个单词开始
            while i >= 0 and s[i] == ' ':
                i -= 1
            # 移动指针j
            j = i
        return ' '.join(res)

if __name__ == "__main__":
    test1 = " I am a stduent. "
    solution = Solution()
    print(solution.reverseWords(test1))