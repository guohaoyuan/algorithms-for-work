"""
首先组成充分条件：
    1. 不能有重复数字;除了大小王之外
    2. 牌中的max - min < 5 除了大小王以外
"""


class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        repeat = set()
        max_ = -float('inf')
        min_ = float('inf')
        for num in nums:
            # 更新最大值最小值
            if num != 0:
                min_ = min(min_, num)
                max_ = max(max_, num)
            else:
                continue

            # 将无重复数字进入repeat
            if num not in repeat:
                repeat.add(num)
            else:
                return False
        return False if max_ - min_ >= 5 else True