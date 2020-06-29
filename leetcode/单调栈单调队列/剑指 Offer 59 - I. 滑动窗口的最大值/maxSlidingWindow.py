"""
单调递增队列,使用双端队列

创建一个返回结果的栈;一个存储索引的双端队列,存储索引,存储索引,存储索引!!!

遍历整个数组:
    需要删除双端队列的头和尾:
                            1. 除头: 如果当前双端队列已经填充了第一个窗口,且队列头部元素超出窗口范围, i >= k-1 and i - queue[0] >= k
                                此时需要将头部元素弹出
                            2. 除尾: 如果双端队列的尾部元素对应值小于等于nums[i],则双端队列尾部元素无出头之日, 直接弹出
    其他情况的下,索引直接进入双端队列
    如果当前i >= k-1
                    将当前双端队列的头部对应值,添加到结果数组中
"""

import collections


class Solution:
    def maxSlidingWindow(self, nums, k):
        if not nums:
            return []
        res = []
        queue = collections.deque()
        n = len(nums)

        for i in range(n):
            # 1.
            if i >= k and i - queue[0] >= k:
                queue.popleft()

            # 2.
            while queue and nums[queue[-1]] <= nums[i]:
                queue.pop()

            queue.append(i)

            if i >= k - 1:
                res.append(nums[queue[0]])
        return res


if __name__ == '__main__':
    nums1 = [7, 2, 4]
    k1 = 2
    solution = Solution()
    print(solution.maxSlidingWindow(nums1, k1))