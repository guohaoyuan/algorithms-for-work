# -*- coding = utf-8 -*-

class Solution(object):

    def findContinuousSequence(self, target):
        """
        滑动窗口：窗口的左边界和右边界永远只能向右移动
        :param target:
        :return:
        """
        # 1. 特殊情况，target不足2
        if target < 2:
            return []

        # 2. 初始化左右边界，中间值，数组和
        small = 1
        big = 2
        arraySum = big + small
        mid = (target + 1) // 2
        res = []

        # 3. 算法流程
        while small < mid:
            # 结束条件
            if arraySum == target:
                res.append(list(range(small, big + 1)))
                # 更新右边界，然后更新数组和,
                big += 1
                arraySum += big
            elif arraySum > target:     # 窗口太大了，先更新数组和，再缩减左边界
                arraySum -= small
                small += 1
            else:                       # 窗口太小了，先扩充右边界，在更新数组和
                big += 1
                arraySum += big
        return res

if __name__ == '__main__':
    test1 = 9
    test2 = 15
    solution = Solution()
    print(solution.findContinuousSequence(test1))
    print(solution.findContinuousSequence(test2))
    '''
    时间复杂度：n，遍历一半的数组
    空间复杂度：?'''