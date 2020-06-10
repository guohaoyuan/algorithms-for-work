# -*- coding : utf-8 -*-

import re

class Solution:
    def myAtoi(self, str):
        # 1. 初始化溢出边界
        int_max = 2**31 - 1
        int_min = - 2**31

        # 2. 删除左侧空格并设置正则化匹配规则
        str = str.lstrip()
        rule = re.compile(r'^[\+\-]?\d+')
        #
        # 按照规则进行匹配
        num = rule.findall(str)

        # 转换为整型
        num = int(*num)

        return max(min(num, int_max), int_min)
if __name__ == "__main__":
    test1 = "412"
    test2 = "    -41"
    test3 = "4193 with words"
    test4 = "-91283472332"
    solution = Solution()
    print(solution.myAtoi(test1))
    print(solution.myAtoi(test2))
    print(solution.myAtoi(test3))
    print(solution.myAtoi(test4))