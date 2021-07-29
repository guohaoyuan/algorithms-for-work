"""
自身^自身=0
0^自身=自身
n是数组的length，我们初始化res = n
然后整个数组的index^数组每一个元素后^n
最后res剩下的数就是结果
"""

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        res = n 

        for i in range(n):
            res ^= i ^ nums[i]
        return res
