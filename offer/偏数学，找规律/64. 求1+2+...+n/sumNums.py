# -*- coding : utf-8 -*-

class Solution:
    def sumNums(self, n):

        return n and n + self.sumNums(n-1)

if __name__ == "__main__":
    n1 = 3
    n2 = 9
    solution = Solution()
    print(solution.sumNums(n1))
    print(solution.sumNums(n2))