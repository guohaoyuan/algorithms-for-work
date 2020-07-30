"""
面试官要求，尽可能快


针对无序数组处理方式，利用哈希表，key存元素，存索引

针对有序数组的处理方式，利用双指针

1. 特殊情况：数组为空，直接返回[]
2. 初始化左右指针L,R=0, n- 1
3. 开始利用二分法寻找
    当两数之和等于目标直接返回
    当两数之和大于目标，搜索区间缩小右边界
    当两数之和小于目标，搜索区间缩小左边界
"""


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:
            return []

        n = len(numbers)
        L, R = 0, n - 1

        while L <= R:
            if L == R:
                return []

            if numbers[L] + numbers[R] == target:
                return [L + 1, R + 1]
            elif numbers[L] + numbers[R] < target:
                L = L + 1
            elif numbers[L] + numbers[R] > target:
                R = R - 1
