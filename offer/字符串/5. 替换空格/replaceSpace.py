# -*- coding : utf-8 -*-

class Solution:
    def replaceSpace(self, s):
        """
        如果是数组可以实现原地修改，是字符串需要辅助空间
        另外有一个更方便的方法，由于创建新空间，从前往后，遇到空格加%20，否则加入对应字符
        :param s:
        :return: 返回一个字符串
        """
        # 1. 特殊情况：字符串为空
        if not s:
            return ""

        # 2. 初始化双指针p1指向原尾巴，p2指向新尾巴
        p1 = len(s) - 1
        count = 0   # 统计空格数目
        res = []    # 存长结果的数组
        # 统计空格数目
        for st in s:
            res.append(st)
            if st == ' ':
                count += 1
        # print("res = {}, count = {}".format(res, count))
        # 扩充数组
        for i in range(count):
            res.append(' ')
            res.append(' ')

        p2 = len(res) - 1
        # print("p1 = {}, p2 = {}".format(p1, p2))
        # 3. 算法流程：在res中从后往前，将p1位置移到p2，其中如果p1遇到空格，则p1前移一位，p2前移3位并添加%20
        # 直到p1p2相遇
        while p1 != p2:
            if res[p1] == ' ':
                p1 -= 1
                res[p2] = '0'
                p2 -= 1
                res[p2] = '2'
                p2 -= 1
                res[p2] = '%'
                p2 -= 1
            else:
                res[p2] = res[p1]
                p1 -= 1
                p2 -= 1
            # print(res)
        return ''.join(res)

if __name__ == '__main__':
    test1 = "we are happy."
    test2 = '  '
    solution = Solution()
    print(solution.replaceSpace(test1))
    print(solution.replaceSpace(test2))
    """
    时间复杂度：n，一次从后向前遍历
    空间复杂度：n，创建了一个返回结果，因为python的字符串为不可变类型"""