"""
先排序，在选择，过程注意排除重复
时间复杂度: n^2， n^2 + nlogn
空间复杂度： n
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 1 特殊情况 数组为空或者长度不足3
        n = len(nums)
        if n < 3:
            return []

        # 2. 初始化res
        res = []
        nums.sort()

        # 3. 算法流程
        for i in range(n):
            # 因为i后面的都会大于0
            if nums[i] > 0:
                return res

            if i > 0 and nums[i] == nums[i - 1]:
                continue
            L = i + 1
            R = n - 1
            while L < R:
                if nums[i] + nums[L] + nums[R] == 0:
                    res.append([nums[i], nums[L], nums[R]])
                    while L < R and nums[L] == nums[L + 1]:
                        L += 1
                    while L < R and nums[R] == nums[R - 1]:
                        R -= 1
                    L += 1
                    R -= 1

                elif nums[i] + nums[L] + nums[R] < 0:
                    L += 1
                elif nums[i] + nums[L] + nums[R] > 0:
                    R -= 1
        return res