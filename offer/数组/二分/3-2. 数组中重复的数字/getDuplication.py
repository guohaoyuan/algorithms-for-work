# -*- coding = utf-8 -*-

class Solution:

    def getDuplication(self, nums):
        """
        不修改原数组，二分法，不按照索引，按照范围中数字数目二分,长度为n，数字范围1~n-1
        :param nums:
        :return: 返回重复数字
        """
        # 1. 特殊情况：数组为空
        if not nums:
            return

        # 2. 初始化左右指针LR
        L = 1
        R = len(nums) - 1

        # 3. 算法流程
        def count_num(nums, L, mid):
            """
            统计L~mid范围数字的数目
            :param nums:
            :param L:
            :param mid:
            :return: 返回数字数目
            """
            # 1. 特殊情况：数组长度为0
            if not nums:
                return 0

            # 2. 初始化计数器
            count = 0

            # 3. 算法流程
            for i in range(len(nums)):
                if nums[i] <= mid and nums[i] >= L:
                    count += 1
            return count

        while L <= R:
            mid = (L + R) // 2
            count = count_num(nums, L, mid)
            # 返回条件是左右指针相遇时，长度大于1
            if L == R:  # 类似归并只剩一个数
                if count > 1:
                    return L
                else:
                    return
            if count > mid - L + 1: # 左侧数字数目>其范围，说明左侧有重复数字，更新右指针为mid，因为mid也可能重复，作为答案
                R = mid
            else:   # 反之就是右侧有重复数字，更新左指针为mid+1，因为mid已经不可能为答案
                L = mid + 1
        return  # 上面结束还没找到，就是没有答案，直接返回

if __name__ == '__main__':
    test1 = [2, 3, 4, 5, 3, 2, 6, 7]
    solution = Solution()
    print(solution.getDuplication(test1))
    '''
    时间复杂度：nlogn，首先二分法logn，其次每个范围都遍历一次数组n，整体nlogn
    空间复杂度：1，常数级别的变量
    '''