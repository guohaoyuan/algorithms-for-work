class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        # 定义初始数组
        res = [0]
        count = 0  # 计数器，方便定位
        m = len(grid)
        n = len(grid[0])

        # 定义感染函数
        def infect(i, j, k):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != 1:
                return
            res[k] += 1
            grid[i][j] = 2
            infect(i - 1, j, k)
            infect(i + 1, j, k)
            infect(i, j - 1, k)
            infect(i, j + 1, k)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    infect(i, j, count)
                    count += 1          # 索引位后移，
                    res.append(0)       # 添加新的初始值

        return max(res)