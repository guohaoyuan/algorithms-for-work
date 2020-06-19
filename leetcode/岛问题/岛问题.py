class Solution:
    def numIslands(self, grid):
        """
        需要问清楚能不能修改原数组
        :param grid:
        :return:
        """
        # 1. 特殊情况:矩阵为空
        if not grid:
            return 0

        # 2. 初始化计数器res,行列
        res = 0
        m = len(grid)
        n = len(grid[0])

        def infect(i, j):
            # 1. 递归终止条件:越界或者当前位置不为1
            if i < 0 or i >= m or j < 0 or j >= n or int(grid[i][j]) != 1:
                return

            # 2. 递归操作,主要是修改1
            grid[i][j] = 2
            infect(i - 1, j)
            infect(i + 1, j)
            infect(i, j - 1)
            infect(i, j + 1)

        # 3. 算法流程双重遍历,如果当前位置为1则计数器++,并执行感染函数
        for i in range(m):
            for j in range(n):
                if int(grid[i][j]) == 1:
                    res += 1
                    infect(i, j)
        return res

    def numIslands_v2(self, grid):
        """
        不修改原输入,我们创建一个新的矩阵,在上面修改
        :param grid:
        :return:
        """

if __name__ == "__main__":
    test1 = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
    solution = Solution()
    print(solution.numIslands(test1))
    print(test1)
    """
    时间复杂度: n^2,
    空间复杂度: 递归空间为1的数目,
    """
