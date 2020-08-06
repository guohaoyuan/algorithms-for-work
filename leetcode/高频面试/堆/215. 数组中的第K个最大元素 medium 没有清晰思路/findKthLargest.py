"""
与剑指offer40类似

方法1：
如果允许修改输入，使用partition函数，结合index与k-1的关系，进行左移右移，再次调用patition函数，

时间复杂度：
            n

方法2：
如果不允许修改输入，也可以使用堆，
1. 先让k个数组成列表进入堆

2. 遍历剩余元素，如果比小顶堆的最小值大，则删除操作，将该数值加入到堆中;
               如果比小顶堆的最小值小，直接跳过这个数值

3. 遍历所有数组，小顶堆里面的就是最大的k个数

时间复杂度：
            (n-k) * logk

"""
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return

            # 建立小顶堆
        tmp = nums[:k]
        heapq.heapify(tmp)

        # 遍历剩余元素，堆顶元素比当前元素大，则跳过;堆顶元素比当前元素小，则入堆
        for i in range(k, len(nums)):
            if nums[i] > tmp[0]:  # 心里记住堆的逻辑结构
                heapq.heappop(tmp)
                heapq.heappush(tmp, nums[i])
            else:
                continue
        return tmp[0]


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 1. 特殊情况：数组为空

        # 2. 初始化左右指针
        L, R = 0, len(nums) - 1

        # 3. 定义partition函数
        def partition(L, R, nums):
            i = L
            j = R
            k = 0
            x = nums[L]

            while i < j:
                while i < j and nums[j] >= x:
                    j -= 1
                if i < j:
                    nums[i] = nums[j]
                    i += 1

                while i < j and nums[i] <= x:
                    i += 1
                if i < j:
                    nums[j] = nums[i]
                    j -= 1

            # i == j
            nums[j] = x
            return i

        index = partition(L, R, nums)

        while index != len(nums) - k:
            if index > len(nums) - k:
                R = index - 1
                index = partition(L, R, nums)
            elif index < len(nums) - k:
                L = index + 1
                index = partition(L, R, nums)
        # index == len(nums) - k
        return nums[index]