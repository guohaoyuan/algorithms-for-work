# -*- coding : utf-8 -*-

class Solution(object):
    def permutation(self, s):
        """
        回溯法；
        :param s:
        :return:
        """
        # 1. 特殊情况：字符串为空
        if not s:
            return []

        # 2. 初始化返回结果res
        res = []
        track = []
        index = []

        # 3. 算法流程定义回溯算法
        def back_track(s, track):
            """

            :param s: 选择列表
            :param track: 路径
            :return:
            """

            # 1. 结束条件：路径长度已经到s长度
            if len(s) == len(track):
                res.append(''.join(track))  # 路径添加到结果中
                return

            # 2. 递归操作
            for i, ch in enumerate(s):    # 在选择列表中做选择
                if i in index:
                    # 不在选择列表中，则加入，在的话跳过
                    continue
                else:
                    index.append(i)
                    track.append(ch)
                # 递归
                back_track(s, track)
                # 撤销选择
                track.pop()
                index.pop()
        # 调用回溯算法
        back_track(s, track)
        res = list(set(res))
        return res

if __name__ == '__main__':
    s1 = "abc"
    s2 = "aab"
    solution = Solution()
    print(solution.permutation(s1))
    print(solution.permutation(s2))
    """
    时间复杂度：n!，时间复杂度和全排列呈现性关系
    空间复杂度：n**2，因为递归是n深度，"""