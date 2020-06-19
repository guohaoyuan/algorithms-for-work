class Solution:
    def subsets(self, nums):
        # 1. 特殊情况: 数组为空,返回空列表
        if not nums:
            return []

        # 2. 初始化返回结果
        res = []
        path = []


        def back_track(path, nums, start):

            res.append(path[:])


            for i in range(start, len(nums)):    # 在选择列表中做选择
                # 做选择
                path.append(nums[i])
                # 递归
                back_track(path, nums, i + 1)
                # 撤销选择
                path.pop()
        # 3. 算法流程

        back_track(path, nums, 0)
        return res
if __name__ == "__main__":
    nums1 = [1, 2, 3]
    solution = Solution()
    print(solution.subsets(nums1))