# -*- coding : utf-8 -*-

import heapq

class Solution:
    def findKthLargest(self, nums, k):
        """
        需要问面试官是否允许原地修改
        :param nums: 数组
        :param k: int第K大的元素
        :return:
        """
        # 1. 特殊情况：数组为空
        if not nums:
            return

        # 2. 初始化：左右指针L R
        n = len(nums)
        L = 0
        R = n - 1

        # 3. 算法流程定义partation

        def partation(nums, L, R):
            """
            快排思想
            :param nums:
            :param L:
            :param R:
            :return:
            """
            i = L
            j = R
            x = nums[L]

            while i < j:
                while i < j and nums[j] > x:    # 注意不稳定排序，不加等号
                    j -= 1
                if i < j:
                    nums[i] = nums[j]
                    i += 1

                while i < j and nums[i] < x:    #
                    i += 1
                if i < j:
                    nums[j] = nums[i]
                    j -= 1
            # 两指针相遇
            nums[i] = x
            # 返回索引
            return i

        # 得到索引
        index = partation(nums, L, R)
        # 不为k进行遍历
        while index != n - k:
            if index < n - k:
                L = index + 1
                index = partation(nums, L, R)
            if index > n - k:
                R = index - 1
                index = partation(nums, L, R)
        return nums[index]
    """
    时间复杂度：平均时间复杂度n，partation函数n，最糟糕的情况为n**2,每次划分都是最大值最小值
    空间复杂度：1
    """


    def findKthLargest_v2(self, nums, k):
        """
        利用堆排序的思路
        1. 特殊情况：是一个空数组，返回
        2. 初始化一个大顶堆，默认为小顶堆，加负号就是大顶堆，大顶堆初始元素为前n-k个数
        3. 遍历range(n - k + 1, n) 因为n-k对应的就是第k个最大元素的索引
            比较-大顶堆顶元素> nums[i]，那么更新大顶堆，先删除堆顶;然后将nums[i]加入大顶堆
        4, 返回堆顶元素
        :param nums:
        :param k:
        :return:
        """

        # 1. 特殊情况：数组为空
        if not nums:
            return

        # 2. 初始化大顶堆
        n = len(nums)
        hp = [-x for x in nums[: (n - k + 1)]]
        heapq.heapify(hp)

        # 3. 算法流程
        for i in range(n - k + 1, n):
            if - hp[0] > nums[i]:
                heapq.heappop(hp)
                heapq.heappush(hp, - nums[i])
        return - hp[0]