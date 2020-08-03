"""
1. 特殊情况：数组为空，直接返回空数组
2. 初始化返回结果数组res,和临时数组path
3. 定义回溯函数
    递归结束条件：没有结束条件，添加所有选择
    递归操作：
            for i in range(len(nums)):
                将当前数加入到path
                递归
                回溯
4. 调用回溯函数
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
                back_track(nums, path, i + 1)       # 传入一个当前索引的后一位能避免重复
                path.pop()
            return
        back_track(nums, path, 0)
        return res