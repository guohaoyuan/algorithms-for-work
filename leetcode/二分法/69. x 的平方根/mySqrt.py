class Solution:

    def mySqrt(self, x):

        if x == 0:
            return 0

        L, R = 0, x

        while L <= R:
            # 这里一定取右中位数,否则可能陷入死循环
            mid = (L+R)//2 + 1
            print(L, mid, R)
            if L == R:
                return L

            if mid * mid < x:
                # 在区间[mid, R]
                L = mid
            elif mid * mid > x:
                # 在区间[L, mid)
                R = mid - 1
            elif mid * mid == x:
                return mid


if __name__ == "__main__":
    x1 = 8
    solution = Solution()
    print(solution.mySqrt(x1))