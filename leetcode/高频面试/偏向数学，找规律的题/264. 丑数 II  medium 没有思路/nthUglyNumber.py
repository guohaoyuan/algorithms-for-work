"""
质因子，简单理解成因子，最基础的因子分解

我们使用一个数组，存放各个丑数，需要三个指针p2 p3 p5，对应的是数组的索引。
每次取得最小的丑数，保证升序，另外指针更新是并行的，不是三选一
"""

class Solution:
    def nthUglyNumber(self, n: int) -> int:

        def helper(n):
            res = [1]
            p2, p3, p5 = 0, 0, 0

            for i in range(1, n):
                ugly = min(res[p2] * 2, res[p3] * 3, res[p5] * 5)
                res.append(ugly)

                if ugly == res[p2] * 2:
                    p2 += 1
                if ugly == res[p3] * 3:
                    p3 += 1
                if ugly == res[p5] * 5:
                    p5 += 1
                print(res)

            return res[n-1]
        res = helper(n)
        return res

if __name__ == '__main__':
    n = 10
    solution = Solution()
    print(solution.nthUglyNumber(n))