"""
1. 特殊情况，数组为空直接返回
2. 初始化一个数组，用于存放当前位置的最大数字res = [0] * len(nums), res[0] = nums[0]
3. for i in range(1, n):
        if res[i-1] + nums[i] > 0:
            res[i] = res[i-1] + nums[i]
        elif:
            res[i] = nums[i]
4. return max(res)
"""