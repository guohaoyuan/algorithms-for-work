"""
两个字：东哥牛逼
"""
class MonotoQueue:
    def __init__(self):
        self.queue = collections.deque()

    def push(self, n):
        # 如果当前入队的元素>双端队列的尾部元素，就压扁小于n的所有元素
        while len(self.queue) > 0 and self.queue[-1] < n:
            self.queue.pop()
        # 压扁操作执行完毕后，进行入队操作
        self.queue.append(n)

    def max_(self):
        # 返回单调队列的头部
        return self.queue[0]

    def pop(self, n):
        # 在队头删除元素n,由于对头元素可能已经在push方法中被压扁，所以不能盲目的popleft;需要判断对头元素是否是n
        if len(self.queue) > 0 and self.queue[0] == n:
            self.queue.popleft()
        # 如果队首元素已经被压扁，就不用执行上面内容了


class Solution:

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        windows = MonotoQueue()
        res = []

        # 遍历整个输入Nums
        for i in range(len(nums)):
            if i < k - 1:
                # 表示先填满前k-1个位置，留下一个位置进行填充
                windows.push(nums[i])
            else:
                # 先把最后一个元素添加进来
                windows.push(nums[i])
                # 添加单调队列的最大值
                res.append(windows.max_())
                windows.pop(nums[i - k + 1])
        return res