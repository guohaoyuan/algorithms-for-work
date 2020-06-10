# -*- coding : utf-8 -*-

class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        要求将数组1扩充
        :param nums1: 数组1,有足够的长度
        :param m: 数组1当前长度
        :param nums2: 数组2
        :param n: 数组2的长度
        :return: 数组1变后
        """
        # 1. 特殊情况：

        # 2. 初始化三个指针：p1指向m，p2指向n，p3指向m+n
        p1 = m - 1
        p2 = n - 1
        p3 = n + m - 1

        # 3. 算法流程：
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] < nums2[p2]:
                nums1[p3] = nums2[p2]
                p3 -= 1
                p2 -= 1
            else:
                nums1[p3] = nums1[p1]
                p3 -= 1
                p1 -= 1
        while p2 >= 0:
            nums1[p2] = nums2[p2]
            p2 -= 1
        # 不需要考虑p1，因为已经在其中
        return

if __name__ == '__main__':
    nums1 = [2, 0]
    nums2 = [1]
    m = 1
    n = 1
    solution = Solution()
    solution.merge(nums1, m, nums2, n)
    print(nums1)
    """
    时间复杂度：n，从后往前，遍历一次
    空间复杂度：1,没有创建新的辅助数组
    """