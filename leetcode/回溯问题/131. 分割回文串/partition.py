class Solution:
    def partition(self, s):
        # 1. 特殊情况: 字符串为空,直接返回空列表
        if not s:
            return []

        # 2. 初始化路径和结果
        res = []
        path =[]
        n = len(s)

        # 3. 算法流程:
        def back_track(path, s, start):
            # 递归终止条件:剩余的为空字符串
            if n == start:
                res.append(path[:])
                return

            #
            for i in range(start, n):
                # 排除不是回文串的情况
                if not palind(s, start, i):
                    continue

                # 做出选择
                path.append(s[start: i + 1])
                back_track(path, s, i + 1)
                path.pop()

        def palind(s, l, r):

            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        back_track(path, s, 0)
        return res

if __name__ =="__main__":
    s1 = "aab"
    solution = Solution()
    print(solution.partition(s1))