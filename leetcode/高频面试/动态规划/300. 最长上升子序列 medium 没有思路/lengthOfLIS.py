"""
细节：上升子序列，必须是严格上升，
    而且得到的是局部最优不是全局最优最优，所以需要最后max

定义状态：
        dp[i]表示以nums[i]结尾的数组上升子序列长度为dp[i]

状态转移方程：
        dp[i] = max(dp[i], dp[j] + 1) ， j in range(i)

base case:
        dp[0] = 1

步骤：
    1. 特殊情况：数组为空，直接返回0
    2.
"""


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 特殊情况：数组为空
        if not nums:
            return 0

        n = len(nums)

        dp = [1 for _ in range(n)]

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

"""
我们利用二分搜索时：
    遇到相等的数，break，跳出来，说明这个数字已经被处理了
    我们的目标是找到>num的数，将其替换掉，而不是<num;抽象理解就是在当前位置维持了一个上升的牌序
利用二分法
有点类似打牌，创建一个空数组res，如果res最后一个元素<当前元素，我们将其入res;
                                否则，我们在牌堆中为其找一个合适的位置，替换掉那个位置的元素，
最后的到的res长度就是最长上升子序列的长度
"""


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        res = []

        for num in nums:
            if not res or res[-1] < num:
                res.append(num)
            else:
                L, R = 0, len(res) - 1
                while L <= R:
                    mid = (L + R) // 2
                    if L == R:
                        res[L] = num
                    if res[mid] > num:
                        # 搜索区间在[L, mid]
                        R = mid
                    elif res[mid] < num:
                        # 搜索区间在[mid + 1, R]
                        L = mid + 1
                    elif res[mid] == num:
                        break
        return len(res)
