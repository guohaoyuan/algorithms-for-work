# -*- coding : utf-8 -*-
import math


class Solution:
    def isPalindrome(self, x):
        """

        :param x: int
        :return: bool
        """
        x = int(x)
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

def isPrime(num):
    num = int(num)
    if num > 1:
        # 查看因子
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            return True

    # 如果输入的数字小于或等于 1，不是质数
    else:
        return False
if __name__=='__main__':
    res = list(map(int, input().split()))
    input_data = [str(x) for x in range(res[0], res[1] + 1)]
    count = 0
    print(input_data)
    solution = Solution()
    for num in input_data:
        tmp1 = solution.isPalindrome(num[:-1])
        tmp2 = isPrime(num[:-1])
        if tmp1 and tmp2:
            count += 1
    print(count)