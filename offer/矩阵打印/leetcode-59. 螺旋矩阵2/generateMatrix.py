# -*- coding : utf-8 -*-

class Solution:
    def generateMatrix(self, n):
        """

        :param n:
        :return:
        """
        # 1. 特殊情况：n = 1
        if n == 1:
            return [[1]]

        # 2. 初始化
        res = [[0 for _ in range(n)] for _ in range(n)]
        t, b, l, r = 0, n - 1, 0, n - 1
        count = 1

        # 3. 算法流程：
        while True:
            for i in range(l, r + 1):
                res[t][i] = count
                count += 1
            t += 1
            if t > b:
                break

            for i in range(t, b + 1):
                res[i][r] = count
                count += 1
            r -= 1
            if l > r:
                break

            for i in range(r, l - 1, -1):
                res[b][i] = count
                count += 1
            b -= 1
            if t > b:
                break

            for i in range(b, t - 1, -1):
                res[i][l] = count
                count += 1
            l += 1
            if l > r:
                break
        return res
if __name__ == '__main__':
    test1 = 3
    solution = Solution()
    print(solution.generateMatrix(test1))