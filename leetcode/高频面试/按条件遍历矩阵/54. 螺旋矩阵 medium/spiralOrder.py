class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 特殊情况：矩阵为空
        if not matrix:
            return []

        # 初始化四个变量和返回结果res
        t, b, l, r = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        m = len(matrix)  # 行
        n = len(matrix)  # 列
        res = []
        while True:
            for i in range(l, r + 1):
                res.append(matrix[t][i])
            t += 1
            if t > b:
                return res

            for i in range(t, b + 1):
                res.append(matrix[i][r])
            r -= 1
            if l > r:
                return res

            for i in range(r, l - 1, -1):
                res.append(matrix[b][i])
            b -= 1
            if t > b:
                return res

            for i in range(b, t - 1, -1):
                res.append(matrix[i][l])
            l += 1
            if l > r:
                return res
