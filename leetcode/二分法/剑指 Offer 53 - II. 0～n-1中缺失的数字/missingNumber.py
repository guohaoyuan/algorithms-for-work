"""
要得就是越界值
"""
class Solution:
    def missingNumber(self, nums):
        # 1. 数组为空
        if not nums:
            return

        # 2. 初始化左右边界L, R
        L, R = 0, len(nums) - 1

        # 3. 二分法
        while L <= R:
            mid = (L + R) // 2
            if nums[mid] == mid:
                # 则缺失数字在右侧区间(mid, R]
                L = mid + 1
            elif nums[mid] != mid:
                # 缺失数字在区间[L, mid)
                R = mid - 1
            # if L == R:
        return L

if __name__ == '__main__':
    test1 = [0, 1, 3]       # 对于缺失中间值的都不需要L==R遍历；主要应对开头缺失和结尾缺失
    test2 = [0,1,2,3,4,5,6,7,9]
    test3 = [0]
    solution = Solution()
    print(solution.missingNumber(test1))
    print(solution.missingNumber(test2))
    print(solution.missingNumber(test3))
    '''
    时间复杂度：logn
    空间复杂度：1
    '''