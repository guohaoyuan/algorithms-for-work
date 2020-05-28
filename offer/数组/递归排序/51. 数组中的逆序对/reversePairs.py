# -*- coding = utf-8 -*-

class Solution(object):

    def reversePairs(self, nums):
        """

        :param nums:
        :return: int逆序对的个数
        """
        # 1. 特殊情况数组长度不足2
        n = len(nums)

        if n < 2:
            return 0

        # 2. 初始化临时数组，左右指针
        tmp = [0 for _ in range(n)]
        L = 0
        R = n - 1

        return self.Merge_sort(nums, L, R, tmp)

    def Merge_sort(self, nums, L, R, tmp):
        leftPairs, rightPairs, crossPairs = 0, 0, 0
        if L < R:
            mid = (L + R) // 2
            leftPairs = self.Merge_sort(nums, L, mid, tmp)
            rightPairs = self.Merge_sort(nums, mid + 1, R, tmp)
            crossPairs = self.merge_array(nums, L, mid, R, tmp)
        return leftPairs + rightPairs + crossPairs

    def merge_array(self, nums, L, mid, R, tmp):
        """
        修改输入
        :param nums:
        :param L:
        :param mid:
        :param R:
        :param tmp:
        :return:
        """
        i = L
        m = mid
        j = mid + 1
        n = R
        k = 0

        count = 0

        while i <= m and j <= n:
            if nums[i] <= nums[j]:  # 稳定排序在于=
                tmp[k] = nums[i]
                k += 1
                i += 1
            else:
                tmp[k] = nums[j]
                k += 1
                j += 1
                count += (mid - i + 1)

        while i <= m:
            tmp[k] = nums[i]
            k += 1
            i += 1

        while j <= n:
            tmp[k] = nums[j]
            k += 1
            j += 1

        for i in range(k):
            nums[L + i] = tmp[i]
        return count



if __name__ == '__main__':
    test1 = [7, 5, 6, 4]
    solution = Solution()
    print(solution.reversePairs(test1))
    '''
    时间复杂度：nlogn，归并排序的时间复杂度
    空间复杂度：n，递归空间复杂度logn，临时数组空间复杂度n，相加为n
    '''