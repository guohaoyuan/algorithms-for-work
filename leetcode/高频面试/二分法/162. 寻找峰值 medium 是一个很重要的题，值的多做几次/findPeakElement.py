"""
数组是无序的，想办法进行二分法
关于判断mid是上升区间还是下降区间，比较mid和mid+1元素
假设mid元素处于上升区间，那我们应该去右侧区间二分查找
假设mid元素处于下降区间，那我们应该去左侧区间二分查找
题目已经说明mid不会存在mid=mid+1
"""

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        if n == 1:
            return nums[0]

        left = 0
        right = n - 1

        while left < right:
            mid = (left + right)>>1
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
            
        return left
