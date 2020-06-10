# -*- coding : utf-8 -*-

class Solution:
    def reverseLeftWords(self, s, n):
        # 1. 特殊情况：字符串为空
        if not s:
            return ""

        # 2. 初始化存储结果的res，字符串长度
        length = len(s)
        res = list(s)

        # 3. 算法流程
        # 定义翻转函数
        def reverse(start, end):
            while start < end:
                res[start], res[end] = res[end], res[start]
                start += 1
                end -= 1

        # 翻转前半端
        reverse(0, n - 1)
        reverse(n, length - 1)
        reverse(0, length - 1)
        return ''.join(res)

if __name__ == "__main__":
    test1 = "abcdefg"
    k1 = 2
    test2 = "lrloseumgh"
    k2 = 6
    solution = Solution()
    print(solution.reverseLeftWords(test1, k1))
    print(solution.reverseLeftWords(test2, k2))