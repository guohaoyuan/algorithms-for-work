# -*- coding : utf-8 -*-

class Solution:
    def isPalindrome(self, x):
        """

        :param x: int
        :return: bool
        """
        # 1. 特殊情况：输入为负数，或者不为零但是结尾为0
        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        # 2. 初始化翻转数字
        reverse = 0

        # 3. 算法流程
        # 当剩余数字>翻转数字时候执行
        # 将余数*10加入到reverse中
        while x > reverse:
            reverse = reverse * 10 + x % 10
            x = x // 10

        # 4. 最终偶数长度 reverse == x ；奇数长度 reverse//10 == x
        return reverse == x or reverse // 10 == x

if __name__=='__main__':
    test1 = 121
    test2 = -121
    test3 = 100
    test4 = 1234321
    test5 = 123321
    solution = Solution()
    print(solution.isPalindrome(test1))
    print(solution.isPalindrome(test2))
    print(solution.isPalindrome(test3))
    print(solution.isPalindrome(test4))
    print(solution.isPalindrome(test5))