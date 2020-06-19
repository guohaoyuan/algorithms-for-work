class Solution:
    def exist(self, board, word):
        # 1. 特殊情况:二维数组为空,返回False
        if not board:
            return False

        # 2. 初始化行列
        m = len(board)
        n = len(board[0])

        # 3. 遍历数组每一个位置
        def dfs(i, j, start):
            # 递归结束条件: 当前长度达到最大,成功匹配;越界或者当前位置字符和匹配比上,则返回F

            if start == len(word):
                return True

            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[start]:
                return False

            # 更改状态,
            tmp = board[i][j]
            board[i][j] = 0

            # 递归操作
            res = dfs(i + 1, j, start + 1) or dfs(i - 1, j, start + 1) or dfs(i, j + 1, start + 1) or dfs(i, j - 1, start + 1)

            # 还原状态
            board[i][j] = tmp
            return res

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False

if __name__ == "__main__":
    board1 = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word1 = "ABCCED"
    word2 = "SEE"
    word3 = "ABCB"
    solution = Solution()
    print(solution.exist(board1, word1))
    """
    时间复杂度: (m * n)^2 递归时间复杂度: m * n, 主函数也是m * n
    空间复杂度: m*n 递归深度m*n
    """