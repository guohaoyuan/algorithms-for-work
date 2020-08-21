"""
以3, 0, 1为例

res ^ (0^3) ^ (1^0) ^ (2^1) = res ^ 3 ^ 2 == 2 所以res = 3

"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        res = n

        for i in range(n):
            res ^= (i ^ nums[i])
        return res