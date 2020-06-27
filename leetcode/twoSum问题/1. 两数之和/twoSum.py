"""
暴力求解:
两层遍历,求解
时间复杂度n^2

引入哈希表,空间换时间
一次遍历即可,
for i in range len nums:

    如果当前元素与target的差值不在字典中,
        将当前元素插入字典中,key: nums[i] value : i
    如果当前元素与target的差值在字典中,
        返回当前元素和差值元素的索引
"""

class Solution:

    def twoSum(self, nums, target):
        # 1. 特殊情况:如果数组为空,返回空列表
        if not nums:
            return []

        # 2. 初始化哈希表
        dic = {}

        # 3, 遍历一次数组
        for i, num in enumerate(nums):
            if target - num not in dic:
                dic[num] = i
            else:
                return [i, dic[target - num]]
        return []


if __name__ == '__main__':
    nums1 = [2, 7, 11, 15]
    target1 = 9
    solution = Solution()
    print(solution.twoSum(nums1, target1))