# -*- coding : utf-8 -*-

class Solution:
    def isStraight(self, nums):
        """

        :param nums: list
        :return: bool
        """
        # 1. 初始化哈希表和最大最小值
        hashmap = {}
        max_value = -1
        min_value = 14

        # 2. 遍历数组
        for num in nums:
            # 遇到大小王跳过
            if num == 0:
                continue

            # 更新最大值和最小值
            max_value = max(max_value, num)
            min_value = min(min_value, num)

            # 如果两者之差>=5，直接返回F
            if max_value - min_value >= 5:
                return False

            # 如果出现重复数字，直接返回F
            if num in hashmap:
                return False

            # 将数字添加至哈希表
            hashmap[num] = num
        return True

    def isStraight_v2(self, nums):
        # 1. 大小王计数器
        poker = 0

        # 2. 排序
        nums.sort()

        # 3. 遍历排序后的数组
        for i in range(4):
            if nums[i] == 0:
                # 如果是大小王，计数器+1
                poker += 1
            else:
                # 不是大小王，就判断是否和下一位相等
                if nums[i] == nums[i + 1]:
                    return False

        return True if nums[4] - nums[poker] < 5 else False

if __name__ == "__main__":
    n1 = [1, 2, 3, 4, 5]
    n2 = [0, 0, 1, 2, 5]
    solution = Solution()
    print(solution.isStraight_v2(n1))
    print(solution.isStraight(n2))
    """
    时间复杂度：n，遍历一次数组
    空间复杂度：n，创建一个哈希表
    """
