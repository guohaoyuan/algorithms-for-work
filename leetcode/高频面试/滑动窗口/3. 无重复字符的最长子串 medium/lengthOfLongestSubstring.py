"""

滑动窗口，
    1. 主要是先更新右边界right,
    2. 当窗口window中出现重复字符
        2.1 更新左边界
    3. 更新当前最长字串的长度
"""

import collections


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 建立有初始值的空窗口哈希表，用于存储滑动过程变化状态
        window = collections.defaultdict(int)

        # 滑动窗口的左右边界，[left, right)
        left, right = 0, 0
        # 字符串长度,
        n = len(s)

        # 当前字符最大长度
        res = 0

        # right 的上界是n
        # 如果右边界没有触底，则执行
        while right < n:
            # 右边界当前字符
            c = s[right]

            # 进入字典
            window[c] += 1

            # 右边界加1
            right += 1

            # 开始移动左边界的条件是window[某个字符多于1]
            while window[c] > 1:
                # 左边界对应字符
                d = s[left]

                # 移除字典
                window[d] -= 1

                # 更新左边界
                left += 1

            # 更新当前长度
            res = max(res, right - left)
        return res


"""
我略纯
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        left, right = 0, 0
        window = collections.defaultdict(int)
        res = 1
        match = 0

        while right < len(s):
            # 移动右指针，试图找到可行解
            # 当前字符
            c1 = s[right]

            window[c1] += 1
            match += 1
            right += 1
            while window[c1] == 2:  # 此时是找到可行解，我们在可行解中找最优解
                # 当前字符
                c2 = s[left]

                # 我们试图破坏这个可行解
                window[c2] -= 1
                match -= 1
                left += 1
            res = max(res, match)
        return res