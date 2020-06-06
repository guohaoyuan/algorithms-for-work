# -*- coding : utf-8 -*-

class Solution:

    def validateStackSequences(self, pushed, poped):
        """

        :param pushed: list
        :param poped: list
        :return: boolean
        """

        # 1. 特殊情况：如果为空直接返回
        if not pushed or not poped:
            return True

        # 2. 初始化辅助栈，辅助栈起始是模拟出栈过程，对应Poped的索引i
        stack = []
        i = 0

        # 3. 算法流程：遍历pushed模拟入栈
        for num in pushed:
            # 入栈过程，判断是否应该出栈
            stack.append(num)
            while stack and stack[-1] == poped[i]:
                stack.pop()
                i += 1
        return not stack
"""
时间复杂度：n,
空间复杂度：n
"""

if __name__ == "__main__":
    pushed1 = [1, 2, 3, 4, 5]
    poped1 = [4, 5, 3, 2, 1]
    solution = Solution()
    print(solution.validateStackSequences(pushed1, poped1))