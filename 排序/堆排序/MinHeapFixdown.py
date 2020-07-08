def minHeapFixdown(nums, i, n):
    """
    i需要调整的索引位
    :param nums:
    :param i:
    :param n:
    :return:
    """
    # 根节点，需要调整的索引位
    tmp = nums[i]

    # 节点i的左孩子索引
    j = 2 * i + 1

    while j < n:
        # 得到左右孩子中最小那个对应的索引位
        if j + 1 < n and nums[j + 1] < nums[j]:
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


def MinHeapDeleteNumber(nums, n):
    nums[0], nums[n - 1] = nums[n - 1], nums[0]
    minHeapFixdown(nums, 0, n - 1)


if __name__ == '__main__':
    nums1 = [0, 15, 30, 40]
    n1 = len(nums1)
    MinHeapDeleteNumber(nums1, n1)
    print(nums1)