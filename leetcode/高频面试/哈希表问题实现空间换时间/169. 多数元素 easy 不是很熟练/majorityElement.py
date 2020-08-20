"""
哈希表实现一个时间复杂度为n;空间复杂度为n
"""


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return

        n = len(nums)
        flag = n // 2
        hashmap = {}

        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1

        for key, value in hashmap.items():
            if value > flag:
                return key

"""
其实是对上面方法的改进
时间复杂度为n
空间复杂度为1
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 摩尔投票
        value = 1
        key = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == key:
                value += 1
            else:
                value -= 1
                if value ==0:
                    # 重置投票的key value
                    key = nums[i]
                    value = 1
        # 多数元素最后
        return key