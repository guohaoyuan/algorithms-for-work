from insort import *


def heapSort(nums):
    if not nums:
        return nums
    n = len(nums)
    tmp = []
    for i in range(n):
        insert(tmp, len(tmp), nums[i])
    return tmp

if __name__ == '__main__':
    nums1 = [90, 70, 80, 60, 10, 40, 50, 30, 20]
    print(heapSort(nums1))