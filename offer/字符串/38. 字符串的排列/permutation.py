# -*- coding : utf-8 -*-
class Solution:
    def permutation(self, s):
        """
        回溯算法
        :param s: str
        :return: list[str]
        """
        # 1. 特殊情况：字符串为空
        if not s:
            return []

        # 2. 初始化返回结果和存放路径的列表
        path = []
        res = []
        index = []

        # 3. 算法流程：
        def helper(s, path):
            if len(path) == 3:
                res.append(''.join(list(path)))
                return

            for i, ch in enumerate(s):
                if i in index:
                    continue
                else:
                    index.append(i)
                    path.append(ch)
                    helper(s, path)
                    path.pop()
                    index.pop()
        helper(s, path)
        res = list(set(res))
        return res

if __name__ == '__main__':
    test1 = "abc"
    test2 = 'aab'
    solution = Solution()
    print(solution.permutation(test1))
    print(solution.permutation(test2))
    """
    时间复杂度：n*n!，全排列时间复杂度n!,复制路径n，整体是n*n!
    空间复杂度：n,不考虑返回结果使用的辅助空间是递归深度n，
    """