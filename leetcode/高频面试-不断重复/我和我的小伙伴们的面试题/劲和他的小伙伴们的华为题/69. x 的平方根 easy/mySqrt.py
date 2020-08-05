"""
经典二分法：
注意会出现一种情况：比如8，会在L = 1,R = 2不停震荡，
此时我们将作如下判断
        if R*R <= x:
            return R
        else:
            :return L


常规二分法思路：
1. 特殊情况：如果当前输入为0,返回0，
            如果当前输入<4,返回1

2. 初始化左右边界L, R = 0, x

3. while L <= R:
    计算mid
    if L == R:
        return L
    # 为了防止死循环
    if R - L == 1:
        if R * R <= x:
            return R
        else:
            return L

    if mid * mid == x:
        :return x
    elif mid * mid < x:
        # 搜索区间[mid, R], 因为小数部分被去掉了，所以就算小于目标x，也是有可能为答案的
        L = mid
    elif mid * mid > x:
        # 搜索区间[L, mid - 1],因为已经大于目标x了，不可能成为答案了
        R = mid -1

"""

class Solution:
    def mySqrt(self, x: int) -> int:
        # 特殊情况
        if x ==0:
            return 0
        if x <= 3:
            return 1

        # 初始化左右边界
        L, R = 1, x

        while L <= R:
            mid = (L + R) >> 1
            if L == R:
                return L
            if R - L == 1:
                if R * R <= x:
                    return R
                else:
                    return L
            if mid * mid == x:
                # 找到目标
                return mid
            elif mid * mid > x:
                # 搜索区间在[L,mid-1]
                R = mid - 1
            elif mid * mid < x:
                # 搜索区间[mid, R],因为要去除小数部分
                L = mid