"""
这个方法太垃圾了,看leetcode liweiwei的方法
"""
import collections

class Solution(object):

    def maxSlidingWindow(self, nums, k):
        """
        立刻想到暴力解法，共有n-k+1个窗口，每个窗口找最大值，总的时间复杂度(n - k + 1)*k
        :param nums:
        :param k:
        :return:
        """
        # 1. 特殊情况：数组非空
        if not nums or k < 0:
            return []

        # 2. 初始化res，索引存储index，滑窗存储deque，
        res = []
        index = collections.deque()
        deque = collections.deque()

        # 3. 算法流程：首先初始化窗口
        for i in range(k):
            # 保证单调递减
            while deque and deque[-1] < nums[i]:
                deque.pop()
                index.pop()
            # 索引和数字都进入队列
            deque.append(nums[i])
            index.append(i)
        res.append(deque[0])

        # 遍历剩余数组
        for i in range(k, len(nums)):
            # 首先更新数组，保证单调递减
            while deque and deque[-1] < nums[i]:
                index.pop()
                deque.pop()
            # 添加数子
            deque.append(nums[i])
            index.append(i)

            # 查看滑窗是否越界
            if index[0] <= i - k:
                index.popleft()
                deque.popleft()
            res.append(deque[0])
        return res
if __name__=='__main__':
    test1 = [1,3,-1,-3,5,3,6,7]
    k1 = 3
    solution = Solution()
    print(solution.maxSlidingWindow(test1, k1))
    '''
    时间复杂度：n，遍历一次数组，维护一个双端队列
    空间复杂度：1
    '''