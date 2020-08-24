"""
这个题需要考虑特殊情况：比如说数组为空，k==0

找最小的k个树，就用大顶堆，在循环中处理小于堆顶的元素

找最大的k个数，就用小顶堆，在循环中处理大于堆顶的元素

步骤：
    1. 特殊情况：数组为空，或者k==0，返回空链表
    2. 取数组的前k个元素，组成一个堆。需要注意是大顶堆，调用函数heapq.heapify(tmp)
    3. 遍历剩余元素，在此过程，
            遇到小于堆顶的元素，就删除堆顶，并将当前元素加入到堆中。调用函数heapq.heappop(tmp)  heapq.heappush(tmp, -arr[i])
            否则，跳过
    4. 返回一个原数组[-x for x in tmp]
"""


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        # 特殊情况：k为0或者
        if not arr or k == 0:
            return []
        # 取前k个元素组成临时列表
        tmp = arr[:k]
        tmp = [-x for x in tmp]
        # 建立大顶堆
        heapq.heapify(tmp)
        n = len(arr)

        # 然后遍历其余的数
        for i in range(k, n):
            if - tmp[0] > arr[i]:
                heapq.heappop(tmp)
                heapq.heappush(tmp, -arr[i])
            else:
                continue
        return [-x for x in tmp]


"""
数据量小的时候
我们利用快排的partition

步骤：
    1. 考虑特殊情况：数组为空或者当前k==0
    2. 实现partition函数
    3. 初始化左右边界，调用partition函数，
    4. while index != k -1:
            考虑搜索边界问题来更新左右边界
    5. 找到合适答案
"""


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        def partition(nums, l, r):
            i = l
            j = r
            x = nums[i]

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

        # 特殊情况
        if not arr or k == 0:
            return []

        # 初始化
        n = len(arr)
        l, r = 0, n - 1
        index = partition(arr, 0, n - 1)
        while index != k - 1:
            if index > k - 1:
                # 搜索区间[l, index -1]
                r = index - 1
                index = partition(arr, l, r)
            elif index < k - 1:
                # 搜索区间[index + 1, r]
                l = index + 1
                index = partition(arr, l, r)
        return arr[:k]