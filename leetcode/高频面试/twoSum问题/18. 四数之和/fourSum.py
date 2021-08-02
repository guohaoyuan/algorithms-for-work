"""
四数之和，

1. 特殊情况：数组为空直接返回[]
2. 初始化res用于存储所有结果
3. 需要两层遍历
for i in range(n-3):    # 需要留出三个位置给后三个数
    需要减枝，去重复,
    if i > 0 and nums[i] == nums[i-1]: continue

    for j in range(i + 1, n-2):需要留出两个位置给后两个数
        需要减枝，去重复
        if j > 0 and nums[j] == nums[j-1]: continue

        利用二分法遍历数组
        while L < R:    #
            四数之和等于目标，添加至结果。另外要避免重复，如果L++后对应的数与前一位相等，则需要继续后移。（所以说多了重复操作就在这）如果R--前的数与后一位相等，则需要继续前移。
            四数之和小于目标，L++
            四数之和大于目标，R--

"""


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(nums)

        if n <= 3:
            return res

        nums.sort()

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                L, R = j + 1, n - 1
                while L <= R:
                    if L == R:
                        break

                    if nums[L] + nums[R] + nums[i] + nums[j] == target:
                        res.append([nums[i], nums[j], nums[L], nums[R]])
                        while L < R and nums[L] == nums[L + 1]:
                            L += 1
                        while L < R and nums[R] == nums[R - 1]:
                            R -= 1
                        L += 1
                        R -= 1
                    elif nums[L] + nums[R] + nums[i] + nums[j] < target:
                        L += 1
                    elif nums[L] + nums[R] + nums[i] + nums[j] > target:
                        R -= 1
        return res
    """
1. 初始化数组的长度n，排除特殊情况n<4的
2. 对数组进行排序
3. 第一层遍历，遍历数组，并初始化元素a=nums[i]
    4. 跳过a重复的情况，nums[i]=nums[i-1]
    5. 第二层遍历,找到b=nums[j], j = i +1，遍历区间不考虑最后两个元素，因为还有c d 
        6. 初始化两个指针L=j+1 R=n-1 ， c= L d=R
        7. 双指针进行遍历，记得排除元素
"""
"""
1. 初始化数组的长度n，排除特殊情况n<4的
2. 对数组进行排序
3. 第一层遍历，遍历数组，并初始化元素a=nums[i]
    4. 跳过a重复的情况，nums[i]=nums[i-1]
    5. 第二层遍历,找到b=nums[j], j = i +1，遍历区间不考虑最后两个元素，因为还有c d 
        6. 初始化两个指针L=j+1 R=n-1 ， c= L d=R
        7. 双指针进行遍历，记得排除元素
"""

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        res = []
        n = len(nums)
        if n < 4:
            return res
        
        nums.sort()

        for i in range(n):
            a = nums[i]

            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            
            for j in range(i + 1, n - 2):
                b = nums[j]

                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                L, R = j + 1, n - 1
                while L < R:
                    c, d = nums[L], nums[R]
                    sum_= a + b + c + d
                    if sum_ == target:
                        res.append([a, b, c, d])
                        while L < R and nums[L] == nums[L + 1]:
                            L += 1
                        while L < R and nums[R] == nums[R - 1]:
                            R -= 1
                        
                        L += 1
                        R -= 1
                    elif sum_ > target:
                        R -= 1
                    else:
                        L += 1
        return res

