"""

步骤
    1. 特殊情况，数组长度不足3,直接返回空列表
    2. 首先对数组进行排序，nums.sort()原地排序
    3. 开始遍历数组
        如果当前元素大于0,直接返回，不可能出现和为0的情况了

        为了防止重复，如果当前元素和前一个元素相等直接跳过（为了防止相等从三个元素入手，都要防止重复，此时是第一重）

        定义L,R指针
        whileL < R
            如果当前元素和满足目标
                将其添加到结果列表res中
                如果L指针与后一位相同，
                    则指针后移
                如果R指针与前一位相同，
                    则指针前移
                L,R分别一位，这是本来就该移位的

            如果当前元素和>目标
                更新右边界
            如果当前元素和<目标
                更新左边界
        返回结果列表res


先排序，在选择，过程注意排除重复
时间复杂度: n^2， n^2 + nlogn
空间复杂度： n
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 1 特殊情况 数组为空或者长度不足3
        n = len(nums)
        if n < 3:
            return []

        # 2. 初始化res
        res = []
        nums.sort()

        # 3. 算法流程
        for i in range(n):
            # 因为i后面的都会大于0
            if nums[i] > 0:
                return res

            if i > 0 and nums[i] == nums[i - 1]:
                continue
            L = i + 1
            R = n - 1
            while L < R:
                if nums[i] + nums[L] + nums[R] == 0:
                    res.append([nums[i], nums[L], nums[R]])
                    while L < R and nums[L] == nums[L + 1]:
                        L += 1
                    while L < R and nums[R] == nums[R - 1]:
                        R -= 1
                    L += 1
                    R -= 1

                elif nums[i] + nums[L] + nums[R] < 0:
                    L += 1
                elif nums[i] + nums[L] + nums[R] > 0:
                    R -= 1
        return res