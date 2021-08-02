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
    
    
    
 """
1. 考虑特殊情况，数组长度低于3，则直接返回空列表。初始化res=[]
2. 对数组进行排序
3. 第一层for循环，用于定位三数之和的a，遍历数组，
    4. 如果数组当前位置元素nums[i]>0，则直接返回
    5. 如果当前a=nums[i]和前一个a=nums[i-1]相等，则i后移一位.
    注释：i - 1表示我已经计算过i-1的情况，如果当前的i重复则直接跳过
         i + 1表示我还没计算i但是我直接后移不正确，因为a=nums[i]和b=nums[i+1]可能相等也是一种情况
    6.初始化b=L=i+1，c=R-1两个数.
    7. 开始利用双指针的方式查找a+b+c=0.
        8. sum_ == 0时候，需要对b c进行去重复。因为R+1会越界，所以使用R - 1 L + 1
        9. 其余情况无需去重复，因为只要a不一样，bc无所谓一样与否
"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        n = len(nums)
        if n < 3:
            return res

        nums.sort()

        for i in range(n):
            a = nums[i]
            if a > 0:
                return res
            
            if i> 0 and nums[i] == nums[i - 1]:
                continue

            L = i + 1
            R = n - 1
            
            while L < R:
                b = nums[L]
                c = nums[R]
                sum_ = a + b + c
                if sum_ == 0:
                    res.append([a, b, c])
                    while L < R and nums[L] == nums[L + 1]:
                        L += 1
                    while R > L and nums[R] == nums[R - 1]:
                        R -= 1
                    
                    
                    L += 1
                    R -= 1
                elif sum_ > 0:
                    R -= 1
                else:
                    L += 1
        return res
