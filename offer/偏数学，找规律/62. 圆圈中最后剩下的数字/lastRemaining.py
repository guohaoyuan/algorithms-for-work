# -*- coding : utf-8 -*-

class Solution:
    def lastRemaining(self, n, m):
        # 1. 初始化res,表示最后存活者的索引
        res = 0

        # if n == 1:
        #     return 0

        # 2. 算法流程：因为我们是倒推，所以从2个人开始
        for i in range(2, n + 1):   # 其中索引表示是人数
            # 模上上一层的人数
            res = (res + m) % i
        return res

if __name__ == "__main__":
    n1 = 5
    m1 = 3
    n2 = 10
    m2 = 17
    solution = Solution()
    print(solution.lastRemaining(n1, m1))
    print(solution.lastRemaining(n2, m2))