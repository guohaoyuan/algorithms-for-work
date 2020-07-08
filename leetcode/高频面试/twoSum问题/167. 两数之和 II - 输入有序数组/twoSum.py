class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 1. 特殊情况
        n = len(numbers)

        if n < 2:
            return []

        res = []

        for i in range(n):
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue
            L = 0
            R = n - 1
            while L < R:
                if numbers[L] + numbers[R] == target:
                    return [L + 1, R + 1]
                    # while L < R and numbers[L] == numbers[L + 1]:
                    #     L += 1
                    # while L < R and numbers[R] == numbers[R - 1]:
                    #     R -= 1
                    # L += 1
                    # R -= 1
                elif numbers[L] + numbers[R] < target:
                    L += 1
                elif numbers[L] + numbers[R] > target:
                    R -= 1
        return res