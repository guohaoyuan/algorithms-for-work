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


"""
"""

class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        # 满足顺子的三个数学条件
        # 出去大小王，最大数-最小数<5;
        # 出去大小王，不能出现重复数字
        tmp = set()
        max_, min_ = -float('inf'), float('inf')
        for num in nums:
            if num == 0:
                continue
            if not tmp or num not in tmp:
                tmp.add(num)
            else:
                return False
            max_ = max(max_, num)
            min_ = min(min_, num)
        if max_ - min_ < 5:
            return True
        else:
            return False