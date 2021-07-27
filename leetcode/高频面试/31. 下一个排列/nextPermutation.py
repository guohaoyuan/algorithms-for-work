"""
1. 我们希望下一个数比当前数大，这样才满足“下一个排列”的定义。因此只需要将后面的「大数」与前面的「小数」交换，就能得到一个更大的数。比如 123456，将 5 和 6 交换就能得到一个更大的数 123465。
2. 我们还希望下一个数增加的幅度尽可能的小，这样才满足“下一个排列与当前排列紧邻“的要求。为了满足这个要求，我们需要：
在尽可能靠右的低位进行交换，需要从后向前查找
将一个 尽可能小的「大数」 与前面的「小数」交换。比如 123465，下一个排列应该把 5 和 4 交换而不是把 6 和 4 交换
将「大数」换到前面后，需要将「大数」后面的所有数重置为升序，升序排列就是最小的排列。以 123465 为例：首先按照上一步，交换 5 和 4，得到 123564；然后需要将 5 之后的数重置为升序，得到 123546。显然 123546 比 123564 更小，123546 就是 123465 的下一个排列

看可视化部分

作者：imageslr
链接：https://leetcode-cn.com/problems/next-permutation/solution/xia-yi-ge-pai-lie-suan-fa-xiang-jie-si-lu-tui-dao-/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 1. 确定i（从倒数第二位开始）和j的index；需要找到第一个升序的i和i + 1，此时j = i + 1 
        i = len(nums) - 2
        
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        
        # 2. 在[j,end]之间找到第一个大于nums[i]的值，nums[k]
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[i] >= nums[j]:
                j -= 1
        # 3. 交换nums[i]和第一个大于nums[i]的元素位置
            nums[i], nums[j] = nums[j], nums[i]

        # 4. 由于[j,end]一定是降序的，那么先逆序[j,end]使之升序
        left, right = i + 1, len(nums) - 1
        # print("left = {}, right = {}".format(left, right))
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


if __name__ == '__main__':
    nums1 = [1, 2, 3]
    solution = Solution()
    solution.nextPermutation(nums1)
