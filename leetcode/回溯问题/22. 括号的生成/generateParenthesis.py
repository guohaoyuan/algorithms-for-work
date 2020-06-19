class Solution:
    """
    性质1: 合法结果,左右括号数目应该一样多
    性质2: 合法结果,对于p[0..i]右括号数目<=左括号数目
    """
    def generateParenthesis(self, n):
        # 1. 特殊情况: n 小于等于0
        if n <= 0:
            return []

        # 2. 初始化路径和结果
        res = []
        path = []

        # 3. 算法流程
        # 为了验证括号的合法性,需要加上left right分别表示剩余左括号和剩余有括号的数目
        def back_track(path, left, right):
            # 递归结束条件有三个:
            # 1. 剩余的左括号多
            # 2. 剩余的左括号或右括号数目<0
            # 3. 剩余的左右括号都为0, 将路径添加res并返回

            if left > right:
                return

            if left < 0 or right < 0:
                return

            if left == 0 and right == 0:
                res.append(''.join(path[:]))
                return

            # 递归操作
            # 做出选择
            path.append('(')
            back_track(path, left - 1, right)
            path.pop()

            path.append(')')
            back_track(path, left, right - 1)
            path.pop()

        back_track(path, n, n)
        return res

if __name__ == "__main__":
    n1 = 3
    solution = Solution()
    print(solution.generateParenthesis(n1))
    """
    时间复杂度: n^4 / n^0.5
    空间复杂度:
    """