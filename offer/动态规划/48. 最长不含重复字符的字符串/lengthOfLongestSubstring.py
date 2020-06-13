# -*- coding : utf-8 -*-

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        首先想到暴力解法，嵌套的遍历找到所有字符串时间复杂度n**2，
        对于每一个字符串利用hashset遍历一次看是否有重复字符，时间复杂度n
        整体时间复杂度n**3
        空间复杂度：m大小的hashset，所有可能出现的字符
        :param s:
        :return:
        """
        # 1. 特殊情况：字符串为空
        if not s:
            return 0

        # 2. 初始化头尾指针，head tail 最大长度res
        head = 0
        tail = 0
        res = 1
        n = len(s)

        # 3. 算法流程：
        # 3.1 首先位置指针tail + 1 对应元素，判断是否在head:tail中
        while tail + 1 < n:
            tail += 1
            # 如果不再其中，将该元素添加到窗口，更新最大长度，和尾指针
            if s[tail] not in s[head: tail]:

                res = max(tail - head + 1, res)

            else:   # 在其中，则右移head指针，一直到该元素不再窗口中
                while s[tail] in s[head: tail]:
                    head += 1
                # 更新尾指针

        return res

    def lengthOfLongestSubstring_v2(self, s):
        """
        滑动窗口+哈希表
        :param s:
        :return:
        """
        # 1. 特殊情况：字符串为空
        if not s:
            return 0

        # 2. 初始化返回结果 哈希表，左指针i
        dic = {}
        res = 0
        i = -1
        n = len(s)

        # 3. 算法流程：遍历一次数组，依次更新左指针，哈希表，返回结果res
        for j in range(n):
            if s[j] in dic:
                i = max(dic[s[j]], i)

            dic[s[j]] = j
            res = max(res, j - i)
        return res

if __name__ == '__main__':
    test1 = "abcabcbb"
    solution = Solution()
    print(solution.lengthOfLongestSubstring(test1))
    """
    时间复杂度：n**2,
    空间复杂度1
    """
    print(solution.lengthOfLongestSubstring_v2(test1))
    """
    时间复杂度：n，遍历一次字符串
    空间复杂度：1，使用哈希表字符串的范围0-127
    """