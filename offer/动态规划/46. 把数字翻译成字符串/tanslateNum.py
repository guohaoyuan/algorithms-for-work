# -*- coding : utf-8 -*-

class Solution:

    def translateNum(self, num):
        """
        有点斐波那契的意思，动态规划
        :param num:
        :return:
        """
        # 1. 特殊情况：输入小于0
        if num < 0:
            return

        # 2. 初始化：先转字符串，求长度
        s = str(num)
        n = len(s)

        one = 1

        if n == 1:
            return one

        two = 2 if '10' <= s[:2] <= '25' else 1
        if n == 2:
            return two

        for i in range(2, n):
            three = one + two if "10" <= s[i-1 : i + 1] <= "25" else two
            one = two
            two = three
        return three

if __name__ == '__main__':
    test1 = 12258
    test2 = 0
    solution = Solution()
    print(solution.translateNum(test1))
    print(solution.translateNum(test2))