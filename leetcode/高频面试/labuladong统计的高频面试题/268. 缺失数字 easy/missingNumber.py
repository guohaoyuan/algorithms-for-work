"""
比如说
index   0   1   2   3(是我们人为添加的)
nums    3   0   1
nums    0   1   0   3

与运算的规律：
    自身^自身=0
    0^自身=自身
"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if not nums:
            return
        res = len(nums)
        for i in range(len(nums)):
            res ^= i ^ nums[i]
        return res