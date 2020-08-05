"""
我们进行原地修改
定义一个感染函数：
        每次遇到1就把上下左右的1都变成2
        当坐标越界或者当前位置不为1就返回

遍历二维矩阵的每一个位置
遇到1
    计数器就加1
    调用感染函数

时间复杂度：m*n
空间复杂度：m*n
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 1. 特殊情况：空数组
        if not grid:
            return 0

        # 2. 初始化，计数器
        count = 0
        m = len(grid)
        n = len(grid[0])
        # 3. 定义感染函数
        def infect(i, j):
            # 递归终止条件：越界或者当前位置不为‘1‘
            if i >= m or i < 0 or j >= n or j < 0 or grid[i][j] != '1':
                return
            grid[i][j] = '2'
            infect(i - 1, j)
            infect(i + 1, j)
            infect(i, j - 1)
            infect(i, j + 1)

        # 遍历数组
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    infect(i, j)


        return count