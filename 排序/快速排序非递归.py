"""
快速排序的思路:
1. 选择一个参考值,
2. 将大于参考值的数放在右侧,小于等于参考值的放在左侧.
3. 对左右两侧重复上面的操作


递归算法主要靠划分子区间,
非递归算使用栈,因为递归本质就是压栈
"""


def partition(l, r, nums):
    i = l
    j = r
    # 挖出来的坑
    x = nums[l]

    # 开始奉承左右两侧
    while i < j:
        while i < j and nums[j] > x:
            j -= 1
        if i < j:   # 此时nums[j] <= x
            nums[i] = nums[j]
            i += 1

        while i < j and nums[i] <= x:
            i += 1
        if i < j:   # 此时nums[i] > x
            nums[j] = nums[i]
            j -= 1

    # i j 相聚
    nums[i] = x
    return i

def QuickSort(nums, left, right):

    s = []

    s.append(left)
    s.append(right)
    while s:
        # 将压入栈的索引依次弹出
        right = s.pop()
        left = s.pop()
        index = partition(left, right, nums)

        if index - 1 > left:
            s.append(left)
            s.append(index - 1)

        if index + 1 < right:
            s.append(index + 1)
            s.append(right)


if __name__ == '__main__':
    nums1 = [5, 4, 3, 2, 1]
    QuickSort(nums1, 0, len(nums1) - 1)
    print(nums1)