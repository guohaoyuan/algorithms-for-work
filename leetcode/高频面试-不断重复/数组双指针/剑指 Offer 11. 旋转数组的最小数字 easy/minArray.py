"""
双指针法，需要比较中间索引和R

while L <= R:
    更新中间指针
    当L==R, 返回结果
    if numbers[mid] < numbers[R]:
        # 搜索区间在[L, mid]
        R = mid
    elif numbers[mid] > numbers[R]:
        # 搜索区间在[mid+1, R]
        L = mid + 1
    elif numbers[mid] == numbers[R]:
        # 搜索区间在[mid, R-1]，比如
        R -= 1

"""

class Solution:
    def minArray(self, numbers: List[int]) -> int:
        # 1. 特殊情况，数组为空
        if not numbers:
            return

            # 2. 初始化左指针，右指针
        L, R = 0, len(numbers) - 1

        while L <= R:
            mid = (L + R) // 2

            # 相遇的情况
            if L == R:
                return numbers[R]
            if numbers[mid] < numbers[R]:
                # 搜索区间在[L, mid]
                R = mid
            elif numbers[mid] > numbers[R]:
                # 搜索区间在[mid+1, R]
                L = mid + 1
            elif numbers[mid] == numbers[R]:
                # 搜索区间在[mid, R-1]
                R -= 1
