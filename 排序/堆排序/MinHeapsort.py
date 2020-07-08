from MinHeapFixdown import *


def heapSort(nums):
    if not nums:
        return nums
    n = len(nums)

    for i in range(n//2 - 1, -1, -1):
        # nums[i], nums[0] = nums[0], nums[i]
        minHeapFixdown(nums, i, n)


if __name__ == '__main__':
    nums1 = [90, 70, 80, 60, 10, 40, 50, 30, 20]
    heapSort(nums1)
    print(nums1)