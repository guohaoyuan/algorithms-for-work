# -*- coding : utf-8 -*-

class Solution:
    def twoSum(self, nums, target):
        """
        立刻想到暴力解法：两层循环，时间复杂度为n**2
        不能满足需要，使用哈希表
        :param nums:
        :param target:
        :return:
        """
        # 1. 特殊情况：输入数组为空
        if not nums:
            return []

        # 2. 初始化哈希表，用字典代替
        hashmap = {}

        # 3. 遍历数组，
        for i, num in enumerate(nums):
            # 当前元素和target的差值不在哈希表中
            if target - num not in hashmap:
                hashmap[num] = i
            else:
                return [hashmap[target - num], i]
        return []

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target1 = 9
    solution = Solution()
    print(solution.twoSum(nums, target1))
    """
    时间复杂度：n
    空间复杂度：n
    """