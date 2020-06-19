class Solution:
    def combine(self, n, k):

        # 1. 特殊情况:两个整数小于等于0,返回空列表
        if n <= 0 or k <= 0:
            return []

        # 2. 初始化返回结果,路径
        path = []
        res = []

        # 3. 算法流程:
        def back_track(path, n, start):
            # 结束条件:因为这里对长度有要求,所以有递归终止条件
            if len(path) == k:
                res.append(path[:])
                return

            # 递归
            for i in range(start, n + 1):
                # 作出选择
                path.append(i)
                # 递归下层
                back_track(path, n, i + 1)
                # 撤销选择
                path.pop()

        back_track(path, n, 1)  # 因为path的元素从1开始
        return res

if __name__ == "__main__":
    n1 = 4
    k1 = 2
    solution = Solution()
    print(solution.combine(n1, k1))