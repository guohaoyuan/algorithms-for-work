# -*- coding : utf-8 -*-

class Solution:

    def __init__(self):
        self.s = ""
        self.dic = {}

    def FirstAppearingOnce(self):
        for st in self.s:
            if st in self.dic and self.dic[st] == 1:
                return st
        return "#"

    def Insert(self, char):
        self.s += char
        if char in self.dic:
            self.dic[char] += 1
        else:
            self.dic[char] = 1

if __name__ == '__main__':
    solution = Solution()
    solution.Insert('g')
    solution.Insert('o')
    print(solution.FirstAppearingOnce())
    solution.Insert('o')
    solution.Insert('g')
    solution.Insert('l')
    solution.Insert('e')
    print(solution.FirstAppearingOnce())