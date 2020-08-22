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
        # 保证Nums1是较短的那一个
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        totalLeft = (m + n + 1) // 2

        # 开始二分法，改变搜索区间的条件：要求交叉关系：
        #   nums1[i-1] <= nums2[j];nums[j-1] <= nums1[i]
        L, R = 0, len(nums1)
        while L < R:
            i = (L + R) >> 1
            j = totalLeft - i
            if nums1[i] < nums2[j - 1]:
                # 为了保证nums1[i] >= nums2[j-1]，搜索区间为[i+1, R]
                L = i + 1
            else:
                # 此时，nums[i] >= nums2[j-1], 因为有可能已经满足条件。搜索区间[L, i]
                R = i

        # 此时L == R,更新i和j
        i = L
        j = totalLeft - i
        # 但是有四种可能的特殊情况,比如,nums1的分割线在最左边，此时i=0,i-1<0. nums1的分割线在最右边，此时i=n,i-1<n.
        nums1Left = nums1[i - 1] if i > 0 else -float('inf')  # 因为我们要找左边的最大值，所以去负无穷
        nums1Right = nums1[i] if i < m else float('inf')  # 因为我们要找右边最小值，所以取正无穷
        nums2Left = nums2[j - 1] if j > 0 else -float('inf')
        nums2Right = nums2[j] if j < n else float('inf')

        if (m + n) & 1 == 1:  # 奇数，中间一个数，取左边的最大值
            return max(nums1Left, nums2Left)
        else:  # 偶数，两数之和、、2
            return (max(nums1Left, nums2Left) + min(nums1Right, nums2Right)) / 2