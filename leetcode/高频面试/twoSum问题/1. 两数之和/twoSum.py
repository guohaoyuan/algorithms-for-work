"""
# 1. 创建一个哈希表，
# 2. 遍历数组nums，如果target-nums[i] 不在哈希表中，则将nums[i]加入哈希表作为key，value设为index
# 3. 在遍历过程中，出现target - nums[i] 在哈希表的情况，返回[i, hashmap[target-nums[i]]]
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}    # key : val = nums[i] : index

        for i, num in enumerate(nums):
            diff = target - num
            if not hashmap or diff not in hashmap:
                hashmap[num] = i
            else:
                return [hashmap[diff], i]
