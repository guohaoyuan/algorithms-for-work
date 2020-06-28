# -*- coding : utf-8 -*-

class Solution:
    def intersect(self, nums1, nums2):
        """
        针对两个数组是有序的情况
        时间复杂度：max(nlogn, mlogm)
        :param nums1: list
        :param nums2: list
        :return: list
        """
        # 1. 特殊情况：其中一个数组为空，就返回[]
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 == 1 or n2 == 1:
            return []

        nums1.sort()
        nums2.sort()

        # 2. 初始化返回列表res 和双指针
        L, R = 0, 0
        res = []

        # 3. 算法流程
        while L < n1 and R < n2:
            if nums1[L] < nums2[R]:
                L += 1
            elif nums1[L] > nums2[R]:
                R += 1
            else:
                res.append(nums1[L])
                L += 1
                R += 1
        return res

    def intersect_v2(self, nums1, nums2):
        """
        是一个数组特别短，另一个数组特别长的情况
        时间复杂度：max(m,n)
        空间复杂度：min(m,n)
        :param nums1:
        :param nums2:
        :return:
        """
        # 1. 特殊情况：其中一个数组为空
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 == 0 or n2 == 0:
            return []

        # 保证第一个位置是较短的数组
        if n1 > n2:
            return self.intersect_v2(nums2, nums1)

        # 2. 初始化哈希表，和nums1中对应位置k
        hashmap = {}
        k = 0

        # 3. 算法流程
        # 遍历较短的数组，填充哈希表
        for i in range(n1):
            if nums1[i] not in hashmap:
                hashmap[nums1[i]] = 1
            else:
                hashmap[nums1[i]] += 1

        # 遍历较长的数组，如果在哈希表中，就缩减value并添加至k
        for i in range(n2):
            if nums2[i] in hashmap and hashmap[nums2[i]] > 0:
                nums1[k] = nums2[i]
                k += 1
                hashmap[nums2[i]] -= 1
        return nums1[:k]

if __name__ == "__main__":
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    solution = Solution()
    print(solution.intersect_v2(nums1, nums2))
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    solution = Solution()
    print(solution.intersect_v2(nums1, nums2))