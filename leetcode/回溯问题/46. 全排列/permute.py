class Solution:
    def permute(self, nums):
        # 1. 特殊情况: 数组为空,则返回空列表
        if not nums:
            return []

        # 2. 初始路径和结果
        res = []
        path = []
        n = len(nums)

        # 3. 算法流程
        def back_track(path, nums):
            # 由于对长度有要求,所以需要有递归结束条件
            if len(path) == n:
                res.append(path[:])
                return

            # 在选择列表中做出选择
            for i in range(n):
                # 因为全排列需要排除已经选择过的数字
                if nums[i] in path:
                    continue

                # 做选择
                path.append(nums[i])

                # 回溯
                back_track(path, nums)

                # 撤销选择
                path.pop()
        back_track(path, nums)
        return res
if __name__ == "__main__":
    nums1 = [1, 2, 3]
    solution = Solution()
    print(solution.permute(nums1))