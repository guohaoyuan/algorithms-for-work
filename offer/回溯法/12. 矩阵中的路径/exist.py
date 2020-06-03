# -*- coding : utf-8 -*-

class Solution:
    def exist(self, board, word):
        """
        利用回溯算法
        :param board:
        :return:
        """
        def dfs(i, j, k):   # 对于字典和字符串，属于外面的变量可以直接调用
            """

            :param i: 行
            :param j: 列
            :param k: 深度，字符串深度
            :return:
            """
            # 1. 递归结束条件：
            # 越界或者不匹配或者回头,由于在递归操作改变的走过路径的中状态'/'，所以回头的情况融合到了不匹配
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]:
                return False
            # k达到word的长度则结束递归
            if k == len(word) - 1:
                return True

            # 2. 递归操作
            # 缓存当前数字便于回溯
            board[i][j], tmp = '/', board[i][j]
            # 调用递归,向四个方向走
            res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
            board[i][j] = tmp
            return res  # 返回字符串是否匹配

        # 1. 特殊情况：题干说明不为空

        # 2. 算法流程：需要先找到开始位置
        for i in range(len(board)):
            for j in range(len(board[0])):
                res = dfs(i, j, 0)
                if res:             # 找到后就返回，不必遍历整个矩阵
                    return True
        return False

if __name__ == '__main__':
    board1 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word1 = "ABCCED"
    board2 = [["a", "b"], ["c", "d"]]
    word2 = "abcd"
    solution = Solution()
    print(solution.exist(board1, word1))
    print(solution.exist(board2, word2))
    """
    时间复杂度：MN*3**k，具体来说，由于不能回头有三个方向选择，字符串长度为k，所以k**3；最糟糕的情况遍历整个矩阵才能找到匹配的字符串MN*k**3
    空间复杂度：k，调用递归函数，深度为字符串长度，最糟糕情况为k=MN
    """