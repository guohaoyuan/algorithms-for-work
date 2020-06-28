"""
1. 我们确定状态dp[i] 表示以nums[i]结尾的数组,最大上升子序列长度

2. base case dp[0] = 1
决定了我们初始化为dp = [1 for _ in range(n)]

3. 我们利用数学归纳/暴力解法,来思考动态转移方程
dp[0] = 1

dp[1] = max(
        dp[0] + 1 if nums[1] > nums[0]
        1
        )

dp[2] = max(
        dp[1] + 1 if nums[2] > nums[1]
        dp[0] + 1 if nums[2] > nums[0]
        1
        )

dp[i] = max(
        dp[i-1] + 1 if nums[i] > nums[i-1]
        ...
        1
        )

for j in range(i):
    dp[i] = max(dp[j] + 1, dp[i])
# 第一次dp[i]=1, 第二次dp[i]表示前两个中最大的, ...

"""


class Solution:

    def lengthOfLIS(self, nums):
        # 1. 特殊情况: 如果数组为空,返回
        n = len(nums)

        if n < 2:
            return n

        # 2. 初始化动态数组
        dp = [1 for _ in range(n)]

        # 3. 算法流程,包括动态转移过程
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])

        return max(dp)


"""
我们考虑二分法:

1. 我们创建一个空列表cell,用于存放上升子序列, 

2. 有点像打扑克牌, 当遇到大于末尾值的牌,我们插入最后.
                 当遇到小于末尾值的排,我们将它插入到合适位置,也就是右侧第一个大于该牌的正上面, 可以理解是被替换掉

3. 最终cell的长度就是上升子序列的长度
"""


class Solution_v2:
    def lengthOfLIS(self, nums):
        # 1. 特殊情况: 数组为空
        n = len(nums)
        if n == 0:
            return

        # 2. 初始化空列表
        cell = []

        # 3. 算法流程,相当于向手中整理扑克牌
        for i in range(n):
            if not cell or cell[-1] < nums[i]:
                cell.append(nums[i])
                print(cell)
            else:
                n_cell = len(cell)
                L, R = 0, n_cell - 1

                while L <= R:
                    mid = (L + R) // 2
                    print(cell, L, R, mid)

                    if L == R:
                        cell[L] = nums[i]
                        break
                    if cell[mid] > nums[i]:
                        # 搜索区间[L, mid]
                        R = mid
                    elif cell[mid] < nums[i]:
                        # 搜索区间(mid, R]
                        L = mid + 1
                    elif cell[mid] == nums[i]:
                        # 搜索区间
                        cell[mid] = nums[i]
                        break

        return len(cell)


if __name__ == '__main__':
    nums1 = [10,9,2,5,3,7,101,18]
    solution = Solution()
    print(solution.lengthOfLIS(nums1))
    nums1 = [10,9,2,5,3,7,101,18]
    nums2 = [4, 10, 4, 3, 8, 9]
    solution_v2 = Solution_v2()
    print(solution_v2.lengthOfLIS(nums1))
    print(solution_v2.lengthOfLIS(nums2))