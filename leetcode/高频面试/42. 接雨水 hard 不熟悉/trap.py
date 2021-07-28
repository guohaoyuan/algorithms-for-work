"""
双指针法：
1. 特殊情况：数组为空返回0
2. 初始化左右指针L,R表示左右索引，返回结果res=0,左边最大的柱子l_max=height[0],右边最大的柱子是r_max=height[n-1]
3. while L <= R:
        #更新左右指针最大柱子
        l_max = max(l_max, height[L])
        r_max = max(r_max, height[R])


        # 找到较小的l_max，该短板将决定左侧的积水量
        if l_max <= r_max:
            res += l_max - height[L]
            L += 1
        # 找到较小的r_max，该短板将决定右侧的积水量
        else:
            res += r_max - height[R]
            R -= 1
4. return res

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        n = len(height)
        res = 0
        L, R = 0, n - 1
        l_max, r_max = height[0], height[n - 1]

        while L <= R:
            # 更新左右最大柱子
            l_max = max(l_max, height[L])
            r_max = max(r_max, height[R])

            # 更新返回值
            if l_max <= r_max:
                # 计算当前位置的水
                res += (l_max - height[L])
                L += 1
            else:
                res += (r_max - height[R])
                R -= 1
        return res
