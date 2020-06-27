"""
如果左右两侧的和小于目标值,则缩减右边界,否则缩减左边界
"""


class Solution:
    def twoSum(self, numbers, target):
        # 1. 特殊情况: 数组为空直接返回空列表
        if not numbers:
            return []

        # 2. 初始化长度, 左右指针
        n = len(numbers)
        L, R = 0, n - 1

        # 3. 算法流程
        while L <= R:
            sum_ = numbers[L] + numbers[R]

            if sum_ > target:
                R = R - 1
            elif sum_ < target:
                L = L + 1
            elif sum_ == target:
                return [L + 1, R + 1]
        return []