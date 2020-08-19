"""
将数组分成左右两部分，需要满足以下两个条件：
    1. 左右两侧的元素个数相等，或者左边元素个数必有元素个数多一个
    2. num1左边最后一个元素<=nums2右边第一个元素；nums1右边第一个元素>=nums2左边最后一个元素

1. 将两个输入调换，保证nums1长度短，nums2长度长
2. 得到两个数组的长度，不用减1
3. 正常情况分割nums1右边第一个元素索引为i;nums2右边第一个元素索引为j
4. 在nums1中进行二分查找，满足上面的两个条件
5. 最后根据奇偶返回结果


"""


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)

        totalLeft = (m + n + 1) // 2

        left, right = 0, m

        while left < right:
            i = (left + right) // 2
            j = totalLeft - i
            if nums2[j - 1] > nums1[i]:
                # 搜索区间[i+1, right]
                # left = i + 1 不会导致陷入死循环
                left = i + 1
            else:
                # 搜索区间[left, i]
                right = i

        i = left
        j = totalLeft - i
        # 存在四种特殊情况，即，nums1的分割线在最右侧或者最左侧;nums2的分割线在最右侧或者最左侧
        nums1LeftMax = nums1[i - 1] if i > 0 else -float('inf')
        nums1RightMin = nums1[i] if i < m else float('inf')
        nums2LeftMax = nums2[j - 1] if j > 0 else -float('inf')
        nums2RightMin = nums2[j] if j < n else float('inf')

        if (m + n) & 1 == 1:
            return max(nums1LeftMax, nums2LeftMax)
        else:
            return (max(nums2LeftMax, nums1LeftMax) + min(nums1RightMin, nums2RightMin)) / 2