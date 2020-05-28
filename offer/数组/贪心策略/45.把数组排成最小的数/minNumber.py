# -*- coding = utf-8 -*-
import functools

class Solution(object):

    def minNumber(self, nums):
        """
        贪心策略
        :param nums:
        :return: 返回一个字符串
        """
        # 1. 特殊情况：数组为空
        if not nums:
            return nums

        # 2. 初始化数组res
        res = [str(x) for x in nums]

        # 3. 定义排序规则
        def sort_cmp(x, y):
            if x + y < y + x:
                return -1
            else:
                return 1

        res.sort(key=functools.cmp_to_key(sort_cmp))
        return ''.join(res)

if __name__ == '__main__':
    test1 = [10, 2]
    test2 = [3, 30, 34, 5, 9]
    solution = Solution()
    print(solution.minNumber(test1))
    print(solution.minNumber(test2))
    '''
    时间复杂度：nlogn，使用排序，最差为n**2，平均时间复杂度为nlogn，n为字符数目
    空间复杂度：n，字符串列表'''