"""
1. 考虑特殊情况：其中一个字符串为空，直接返回空字符串
2. 初始化两个字典，一个存储目标needs,一个存储当前窗口，初始化窗口的左右指针 0 0
 ，初始化最短数组长度minLen，初始化一个匹配变量match（表示匹配上的字符个数，t的字符不重复，
                                                当match的大小等于t的长度，则可能是解，但是不一定最优解）
3. 当右指针<len(s)
        移动右指针right
        如果右指针指向的字符在needs中，则window加入这个字符。
            如果window和needs对应字符的数目匹配上，则更新匹配match
        当match匹配上t的长度
            如果当前长度小于minLen,则需要更新开始位置，和字符串子集的长度

            接下来更新左指针，如果左指针对应的字符在needs中，则window这个字符-1;
                如果window中这个字符的数目<needs中这个字符的数目
                    match -=1
                更新左指针
4. 在返回结果处，需要判断当前最小长度是否为初始值，不为初始值，就返回s[start:start+minLen]


"""

import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 特殊情况
        if not s or not t:
            return ""

        # 初始化窗口的左右指针，动态窗口和目标窗口，match用于表示t的长度匹配度
        left, right = 0, 0
        match = 0
        needs = collections.defaultdict(int)
        window = collections.defaultdict(int)
        n = len(s)
        start = 0
        for c in t:
            needs[c] += 1
        minLen = float('inf')
        # 两重while 外层用于移动右指针，内层移动左指针
        while right < n:
            # 当前字符
            c1 = s[right]
            if c1 in needs:
                # 如果当前字符是目标字符，则进入window
                window[c1] += 1
                # 当前字符满足匹配条件
                if window[c1] == needs[c1]:
                    match += 1
            right += 1

            # 第二重循环，开始更新左指针
            while match == len(needs):      # 小细节：字符串可能有重复，单哈希表的key不会重复
                # 满足匹配度，我们更新最优解
                if right - left < minLen:
                    start = left
                    minLen = right - left
                # 当前左指针的字符
                c2 = s[left]
                # 如果当前字符是目标字符，尝试破坏这个条件，为了找到最优解
                if c2 in needs:
                    window[c2] -= 1
                    # 满足破坏条件
                    if window[c2] < needs[c2]:
                        match -= 1
                left += 1
        return "" if minLen == float('inf') else s[start: start + minLen]

if __name__ == '__main__':
    S = "ADOBECODEBANC"
    T = "ABC"
    solution = Solution()
    print(solution.minWindow(S, T))
    # from collections import Counter
    #
    # colors = ['red', 'blue', 'red', 'green', 'blue', 'blue']
    # c = Counter(colors)
    # print(dict(c))
