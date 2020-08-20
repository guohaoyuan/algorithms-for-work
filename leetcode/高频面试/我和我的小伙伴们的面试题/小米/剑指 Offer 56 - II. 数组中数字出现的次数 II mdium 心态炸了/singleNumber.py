"""
1. 建立了一个数组array32长度，存储每一位1的数目
2. 然后遍历数组array进行移位相加，进行移位相加


总结：在位运算，会遇到一个mask标志位 & 某一个数字num看对应位是不是1,应该是>0.而非==1
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 1.特殊情况
        if not nums:
            return

            # 2. 创建一个数组存储int的长度,4字节，32位
        array = [0 for _ in range(32)]
        # 表示的物理含义就是高位到低位

        # 将每一个num的每一位都加起来，这样出现三次的数，
        # 对应位置能被3整除，而余数就是只出现一次的数
        for num in nums:
            # 做与运算的标志位
            mask = 1
            for j in range(31, -1, -1):
                if mask & num > 0:
                    array[j] += 1
                mask <<= 1
        res = 0  # 一开始的0经过32次左移到达33的位
        for flag in array:
            res <<= 1
            tmp = flag % 3
            res += tmp
        return res