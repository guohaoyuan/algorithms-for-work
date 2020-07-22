"""
有点类似归并排序，需要用到双指针

步骤
    1. 如果m=0直接将nums2复制过去;如果n=0直接返回nums1
    2. 初始化两个指针p1 -> nums1 p2 -> nums2, p3 -> m + n -1
    3. p1 p2 >= 0:
           如果p1 >= p2
                    nums1[p3] = nums1[p1]
                    p3-=1
                    p1-=1
           如果p1 < p2
                    nums1[p3] = nums2[p2]
                    p3-=1
                    p2-=1
        p2 >= 0
                nums1[p3] = nums2[p2]
                p3-=1
                p2-=1
"""


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return nums1

        # 初始化三个指针
        p1 = m - 1
        p2 = n - 1
        p3 = n + m - 1

        # 算法流程
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] >= nums2[p2]:
                nums1[p3] = nums1[p1]
                p3 -= 1
                p1 -= 1
            else:
                nums1[p3] = nums2[p2]
                p3 -= 1
                p2 -= 1
        while p2 >= 0:
            nums1[p3] = nums2[p2]
            p3 -= 1
            p2 -= 1
        return nums1