"""
利用堆
"""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        tmp = nums[:k]
        heapq.heapify(tmp)
        n = len(nums)

        for i in range(k, n):
            if tmp[0] <= nums[i]:
                heapq.heappop(tmp)
                heapq.heappush(tmp, nums[i])
            else:
                continue
        return tmp[0]

"""
partition
"""


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(nums, l, r):
            i = l
            j = r
            k = 0
            x = nums[l]

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
            nums[i] = x
            return i

        n = len(nums)
        k = n - k
        L, R = 0, n - 1
        index = partition(nums, 0, n - 1)

        while index != k:
            if index < k:
                # 搜索区间[index + 1, R]
                L = index + 1
                index = partition(nums, L, R)
            elif index > k:
                # 搜索区间[L, index - 1]
                R = index - 1
                index = partition(nums, L, R)
        return nums[index]