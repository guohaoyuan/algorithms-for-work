# -*- coding : utf-8 -*-

class Solution:

    def spiralOrder(self, matrix):
        """

        :param matrix:
        :return: 一个list
        """
        # 1. 特殊情况：矩阵为空
        if not matrix:
            return []

        # 2. 初始化上下左右边界
        t, b, l, r = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        res = []

        # 3. 算法流程
        while True:
            for i in range(l, r + 1):
                res.append(matrix[t][i])
            t += 1
            if t > b:
                break

            for i in range(t, b + 1):
                res.append(matrix[i][r])
            r -= 1
            if l > r:
                break


            for i in range(r, l - 1, -1):
                res.append(matrix[b][i])
            b -= 1
            if t > b:
                break

            for i in range(b, t - 1, -1):
                res.append(matrix[i][l])
            l += 1
            if l > r:
                break
        return res