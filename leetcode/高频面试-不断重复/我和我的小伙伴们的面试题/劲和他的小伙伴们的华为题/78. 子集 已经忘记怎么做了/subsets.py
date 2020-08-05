"""
子集问题较为特殊，、
他的结束条件，
不是在回溯算法的一开始就确定，
而是在for循环中，发现长度不够，自动结束了
"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        res = []
        path = []

        def back_track(nums, path, start):
            res.append(path[:])

            for i in range(start, len(nums)):
                path.append(nums[i])
                back_track(nums, path, i + 1)
                path.pop()

        back_track(nums, path, 0)
        return res