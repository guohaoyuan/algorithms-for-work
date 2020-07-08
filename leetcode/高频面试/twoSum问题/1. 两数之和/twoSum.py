"""
使用哈希表： 空间换时间

"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1. 特殊情况：数组为空
        if not nums:
            return []

        # 2. 初始化哈希表
        hashmap = {}
        n = len(nums)

        # 3. 算法流程
        for i in range(n):
            # 如果目标和当前数的差不再hash中，添加当前数
            if target - nums[i] not in hashmap:
                hashmap[nums[i]] = i
            else:
                return [i, hashmap[target - nums[i]]]