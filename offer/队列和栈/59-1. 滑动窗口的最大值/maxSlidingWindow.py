# -*- coding : utf-8 -*-

import collections

class Solution:

    def maxSlidingWindow(self, nums, k):
        """
        首先想到暴力解法，时间复杂度nk
        我们选择滑动窗口法，时间复杂度n
        :param nums: list
        :param k: int
        :return: list
        """
        # 1. 特殊情况：列表为空或者k小于0
        if not nums or k < 0:
            return []

        # 2. 初始化变量：一个双端队列维护滑动窗口最大值；一个双端队列维护对应的索引，一个列表存储返回值
        res = []
        max_queue = collections.deque()
        max_index = collections.deque()

        # 3. 算法流程
        # 3.1 先初始化第一个滑窗
        for i in range(k):
            # 保证队列单调递减，否则需要删除队列尾巴的元素
            while max_queue and max_queue[-1] < nums[i]:
                max_queue.pop()
                max_index.pop()
            if not max_queue or max_queue[-1] >= nums[i]:
                max_queue.append(nums[i])
                max_index.append(i)

        res.append(max_queue[0])


        # 3.2 从k开始遍历nums，更新滑窗
        for i in range(k, len(nums)):
            # 保证队列单调递减，否则需要删除尾巴元素
            while max_queue and max_queue[-1] < nums[i]:
                max_queue.pop()
                max_index.pop()

            if not max_queue or max_queue[-1] >= nums[i]:
                max_queue.append(nums[i])
                max_index.append(i)

            # 需要维护双端队列的索引不能越界
            if max_index[0] <= i - k:
                max_queue.popleft()
                max_index.popleft()



            res.append(max_queue[0])
        return res

if __name__=='__main__':
    test1 = [1,3,-1,-3,5,3,6,7]
    k1 = 3
    test2 = [1, -1]
    k2 = 1
    solution = Solution()
    print(solution.maxSlidingWindow(test1, k1))
    print(solution.maxSlidingWindow(test2, k2))

    '''
    时间复杂度：n，遍历一次数组，维护一个双端队列
    空间复杂度：1
    '''