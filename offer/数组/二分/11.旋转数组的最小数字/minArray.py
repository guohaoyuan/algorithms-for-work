# -*- coding = utf-8 -*-

class Solution(object):

    def minArray(self, numbers):
        """
        有序数组采用了二分法
        :param numbers: 是一个旋转数组
        :return: 返回值旋转点
        """
        # 1. 特殊情况 数组为空
        if not numbers:
            return

        # 2. 初始左右指针
        L = 0
        R = len(numbers) - 1

        # 3. 算法流程
        while L < R:
            mid = (L + R) // 2

            # 例如 [5, 1, 2, 3, 4]，最小值在区间[L, mid]
            if numbers[mid] < numbers[R]:
                R = mid

            # 例如 [2, 3, 4, 5, 1], 最小值在区间(mid, R]
            elif numbers[mid] > numbers[R]:
                L = mid + 1

            # 例如 [1, 0, 1, 1, 1] [1, 1, 1, 0, 1]
            elif numbers[mid] == numbers[R]:
                # 不能分清,mid属于哪一侧, 最小值在[L, R)
                R = R - 1
        return numbers[L]   # 三点收敛

if __name__ == '__main__':
    test1 = [3, 4, 5, 1, 2]
    test2 = [2, 2, 2, 0, 1]
    solution = Solution()
    print(solution.minArray(test1))
    print(solution.minArray(test2))
    '''
    时间复杂度：logn，当数组元素一样n，不一样时logn
    空间复杂度：1
    '''