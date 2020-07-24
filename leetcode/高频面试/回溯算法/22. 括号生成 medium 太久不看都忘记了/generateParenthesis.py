"""
回溯法的框架：
    1. 定义backtrack(res, left, right):
        传入左括号数目和有括号的数目，
        结束条件：有三个，
                1. 剩余左括号数目大于剩余有括号数目，直接返回。因为目前path中已有的左括号应该小于已有的右括号。
                2. 剩余左括号数目等于0,剩余有括号数目等于0，将当前路径加入到res中
                3. 如果其中一个括号的数目小于0了，则直接返回

        我们不再使用for进行选择，
                1.选择左括号，
                2. 递归调用backtack(res, left-1,right)
                3. 撤销选择path.pop()

                4. 选择右括号
                5. 递归调用backtrack(res, left, right-1)
                6. 撤销选择path.pop()
"""


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 考虑特殊情况：
        if n == 0:
            return []

        # 初始化返回结果和路径
        res = []
        path = []

        def backTrack(path, left, right):
            # 如果剩余左括号大于剩余右括号返回
            if left > right:
                return

            # 如果两者同时为0
            if left == 0 and right == 0:
                res.append(''.join(path[:]))
                return

            # 如果有一个小于0
            if left < 0 or right < 0:
                return

            # 选择
            path.append("(")
            backTrack(path, left - 1, right)
            path.pop()

            path.append(")")
            backTrack(path, left, right - 1)
            path.pop()

        backTrack(path, n, n)
        return res