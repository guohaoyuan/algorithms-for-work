class Solution:
    def combinationSum(self, candidates, target):
        # 1. 特殊情况: 数组为空,或者目标<=0
        if not candidates or target <= 0:
            return []

        # 2. 初始化路径和res
        res = []
        path = []
        # 排序是为了,从前往后不出现重复的选择
        candidates.sort()
        n = len(candidates)

        # 3. 算法流程,
        def back_track(path, candidates, residual, index):
            # 剩余的残差为0
            if residual == 0:
                res.append(path[:])
                return

            #
            for i in range(index, n):
                # 是将不满足条件的排除,减枝
                if residual - candidates[i] < 0:
                    break
                path.append(candidates[i])
                back_track(path, candidates, residual - candidates[i], i)
                path.pop()
        back_track(path, candidates, target, 0)
        return res

if __name__ == "__main__":
    candidates1 = [2, 3, 6, 7]
    target1 = 7
    solution = Solution()
    print(solution.combinationSum(candidates1, target1))
    candidates2 =[2, 3, 5]
    target2 = 8
    print(solution.combinationSum(candidates2, target2))