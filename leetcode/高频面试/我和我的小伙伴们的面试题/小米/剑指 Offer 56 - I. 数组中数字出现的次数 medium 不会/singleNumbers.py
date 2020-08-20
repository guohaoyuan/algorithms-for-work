"""
需要进行两次遍历
1. 第一次遍历是为了找到一个标志位flag将Nums分成两组
        包括： 1.1 遍历全部数组异或，得到tmp
              1.2 利用while找到第一个1的位，作为flag

2. 第二次遍历是为了将nums，按照flag分成两组进行异或。得到的a,b就是结果
        分组的依据是：flag&num >0 是一组， =0是另一组
"""


class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        # 用于存储整个数组异或的结果
        tmp = 0
        for num in nums:
            tmp ^= num

        # 在tmp上找到第一个不是0的位，作为分类的标准
        flag = 1
        while tmp & flag == 0:
            flag = flag << 1
        a, b = 0, 0
        # 第二次遍历进行分组
        for num in nums:
            if flag & num > 0:  # 不应该等于1作为判断，因为flag = 100; num = 101;与运算得到4并不是1
                a ^= num
            else:
                b ^= num
        return [a, b]