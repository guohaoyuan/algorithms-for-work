class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 特殊情况
        if not nums:
            return []

        nums.sort()
        # 初始化
        res = []
        n = len(nums)
        for i in range(n - 3):
            # 对于外层循环，需要进行减枝，以免重复
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):

                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                L, R = j + 1, len(nums) - 1

                while L < R:
                    tmp = nums[i] + nums[j] + nums[L] + nums[R]
                    if tmp == target:
                        res.append([nums[i], nums[j], nums[L], nums[R]])
                        while L < R and nums[L] == nums[L + 1]:
                            L += 1
                        while L < R and nums[R] == nums[R - 1]:
                            R -= 1
                        L += 1
                        R -= 1
                    elif tmp < target:
                        L += 1
                    elif tmp > target:
                        R -= 1
        return res