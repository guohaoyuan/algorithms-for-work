"""
统一输入
"""
def down(nums, start, end):
    """

    :param nums:
    :param start: 开始索引
    :param end: 结束索引
    :return:
    """
    # 根节点，需要调整的索引位
    i = start
    tmp = nums[i]

    # 节点i的左孩子索引
    j = 2 * i + 1

    while j <= end:
        # 得到左右孩子中最小那个对应的索引位
        if j + 1 < end and nums[j + 1] < nums[j]:
            j += 1

        # 如果孩子节点大于根节点i则已经有序
        if nums[j] > tmp:
            break

        # 较小的节点i向下沉，较大的子节点向上升
        nums[i] = nums[j]
        i = j   # 更新当前索引的位置
        j = 2 * i + 1

    # 为原始根节点找到位置
    nums[i] = tmp


def detele(nums, n):
    nums[0], nums[n - 1] = nums[n - 1], nums[0]
    # 堆的删除操作，先交换堆顶和表层元素，然后调整0..n-1个元素的堆，n-1表示的是长度
    down(nums, 0, n - 2)


if __name__ == '__main__':
    nums1 = [0, 15, 30, 40]
    n1 = len(nums1)
    detele(nums1, n1)
    print(nums1)