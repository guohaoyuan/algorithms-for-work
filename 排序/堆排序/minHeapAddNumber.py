def MinHeapFixUp(nums, i):
    """
    将新节点i插入到数组nums中,
    新节点i的父节点(i-1)/2
    :param nums:
    :param i: index需要调整的索引位
    :return:
    """
    # 获得父节点的索引
    j = (i - 1) // 2

    # 待插入节点小于父节点到根节点的元素
    while j >= 0 and nums[i] < nums[j]:
        nums[i], nums[j] = nums[j], nums[i]

        # 上面的交换，导致插入元素索引发生变化
        # 继续更新元素nums[i]的索引和父节点索引
        i = j
        j = (i - 1) // 2


def Minadd(nums, n, nNum):
    nums.append(nNum)
    # 添加一个元素，所以是n
    MinHeapFixUp(nums, n)


if __name__ == '__main__':
    nums1 = [10, 40, 30]
    n1 = 3
    nNum1 = 15
    Minadd(nums1, n1, nNum1)
    print(nums1)