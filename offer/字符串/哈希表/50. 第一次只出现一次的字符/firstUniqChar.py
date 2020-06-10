# -*- coding : utf-8 -*-

class Solution:
    def firstUniqChar(self, s):
        """
        使用哈希表，遍历两次，
        第一次遍历得到对应字符和布尔值是否多次出现
        第二次遍历得到第一个布尔值False
        :return:
        """
        # 1. 特殊情况：字符串为空
        if not s:
            return " "

        # 2. 初始化哈希表
        dic = {}

        # 3. 算法流程：两次遍历
        # 第一次遍历，统计出现次数
        for st in s:
            if st in dic:
                dic[st] = True
            else:
                dic[st] = False

        # 第二次遍历，寻找第一个出现True
        for key, value in dic.items():
            if value == True:
                return key
        return " "
if __name__ == '__main__':
    """
    时间复杂度：n，尽管遍历了两次，
    空间复杂度：1，,ascci码，占128或者256,常数级别空间复杂度
    """