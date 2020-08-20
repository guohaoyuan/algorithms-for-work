"""
思路是进行置换：
比如:
index:  0   1   2   3
nums:   3   4   -1  1
nums:   -1  4   3   1
nums:   -1  1   3   4
nums:   1   -1  3   4
进行置换的条件是：   1. 现将index=0的3放在对应位值index=2
                  2. 此时index=0的元素为-1,但因为不在[0, len]之间，所以不再改变。进入下一个数字
                  3. index=1的元素4放在index=3，此时index=1对应元素为1，仍然需要置换到index=0的位置;
                  得到index=0对应1,index=1对应-1.进入下一个数字
                  4. index=2为3,进入下一个数字。。。。。
"""


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 1

        n = len(nums)

        #
        for i in range(n):
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:  # 就是说待交换的两个数字不能相等，以免陷入死循环
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1] # 交换有先后顺序，另外list是可变的

        # 第二次遍历数组，找到索引与元素不对应的元素
        for i in range(n):
            if i != nums[i] - 1:
                return i + 1  # 就向情况2，3
        return n + 1  # 否则就像情况1
if __name__ == '__main__':
    nums = [3,4,-1,1]
    solution = Solution()
    print(solution.firstMissingPositive(nums))