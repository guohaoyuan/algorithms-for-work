"""
插入节点，是插入到表层，然后上升过程
"""

def up(nums, end):
    """

    :param nums:
    :param end: 结束索引
    :return:
    """
    j = end
    # 获得父节点的索引
    i = (j - 1) // 2

    # 待插入节点小于父节点到根节点的元素
    while i >= 0 and nums[j] < nums[i]:
        nums[i], nums[j] = nums[j], nums[i]

        # 上面的交换，导致插入元素索引发生变化
        # 继续更新元素nums[i]的索引和父节点索引
        j = i
        i = (j - 1) // 2


def insert(nums, n, num):
    nums.append(num)
    # 新加的元素在表层，即n
    up(nums, n)


if __name__ == '__main__':
    nums1 = [10, 40, 30]
    n1 = 3
    nNum1 = 15
    insert(nums1, n1, nNum1)
    print(nums1)