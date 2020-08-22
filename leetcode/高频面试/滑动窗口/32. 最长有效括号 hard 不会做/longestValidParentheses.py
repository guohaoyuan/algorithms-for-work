"""
可以理解成两次滑动窗口吧
时间复杂度：n
空间复杂度：1


比如:
index   0   1   2   3   4   5   6
nums    (   )   (   (   (   )   )
-->
正向遍历：
left, right = 0, 0
如果当前遇到(:    left ++
如果当前遇到):    right ++
当left < right:  left = 0 right = 0将左右括号数目置零
当left == right: max_len = max(max_len, left*2)

index = 2   对应的(导致我们的max_len只能为4

<--
反向遍历：
left, right = 0, 0
如果当前遇到(:    left ++
如果当前遇到):    right ++
当left > right: left, right = 0, 0将左右括号置0.根正向遍历相反
当left == right: max_len = max(max_len, left*2)

return max_len

"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        #   (   )   (   (   (   )   )
        if not s:
            return 0
        max_len = 0
        left, right = 0, 0
        for i in range(len(s)):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if right > left:
                # )()
                left, right = 0, 0
            if left == right and max_len < 2*left:
                # 此时八成是匹配了
                max_len = left*2
        left, right = 0, 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if left > right:
                left, right = 0, 0
            if left == right and max_len < 2*left:
                max_len = left*2
        return max_len