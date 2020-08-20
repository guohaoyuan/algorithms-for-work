"""
遍历两次，利用哈希表存储key:value
    其中key代表数字;value代表数字是否多次出现,True出现一次;False多次出现。


"""

class Solution:
    def firstUniqChar(self, s: str) -> str:
        if not s:
            return " "
        hashmap = {}
        for c in s:
            if c not in hashmap:
                # 表示第一次出现
                hashmap[c] = True
            else:
                # 表示多次出现
                hashmap[c] = False
        for c in s:
            if hashmap[c]:
                return c
        else:
            return " "