# -*- coding = utf-8 -*-

class Solution:

    def search(self, nums, target):
        """
        使用二分法，
        :param nums:
        :param target:
        :return:
        """
        # 1. 特殊情况：数组为空
        n = len(nums)

        if n == 0:
            return

        # 2. 初始化左右指针和起始位置，终止位置
        L = 0
        R = n - 1
        firstPosition, lastPosition = 0, 0

        # 3. 算法流程，定义两个函数
        def find_first_position(nums, L, R):
            while L <= R:
                mid = (L + R) // 2
                if nums[mid] == target:
                    if (mid - 1 >= 0) and (nums[mid - 1] == target):    # 不越界且目标值在L ~ mid - 1闭区间
                        R = mid - 1
                    else:   # 表示不相等，不存在起始位置
                        return mid

                elif nums[mid] > target:    # 目标值在L ~ mid - 1闭区间
                    R = mid - 1
                else:                       # 目标值在 mid + 1 ~ R闭区间
                    L = mid + 1

            return L

        def find_last_position(nums, L, R):
            while L <= R:
                mid = (L + R) // 2
                if nums[mid] == target:
                    if (mid + 1 <= R) and (nums[mid + 1] == target):    # 不越界且目标值在mid + 1 ~ R闭区间上
                        L = mid + 1
                    else:       # 不存在终止位置
                        return mid

                elif nums[mid] > target:    # 目标值在L ~ mid - 1闭区间上
                    R = mid - 1
                else:                       # 目标值在mid + 1 ~ R闭区间上
                    L = mid + 1

            return L

        firstPosition = find_first_position(nums, L, R)
        lastPosition = find_last_position(nums, L, R)

        # 目标值是否存在
        if nums[firstPosition] != target:
            return 0

        return lastPosition - firstPosition + 1

if __name__ == '__main__':
    test1 = [5,7,7,8,8,10]
    target1 = 8
    test2 = [5,7,7,8,8,10]
    target2 = 6
    solution = Solution()
    print(solution.search(test1, target1))
    print(solution.search(test2, target2))
    '''
    时间复杂度：logn，二分法
    空间复杂度：1，常数级别的变量
    '''