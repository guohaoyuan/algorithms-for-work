"""
思想：
    将数组nums划分为nums[0..i] nums[i+1..n-1]
    前面为有序区，后面为无序区，将i+1..n-1中最小值插入到有序区的最后
"""

def SelectSort(nums):
    n = len(nums)

    if not nums:
        return nums

    for i in range(n):
        # 初始化最小值索引
        nMin = i
        # 找到i+1..n-1中最小值所在索引
        for j in range(i + 1, n):
            if nums[j] < nums[nMin]:
                nMin = j

        # 将最小值索引所在位置放到有序区后
        nums[i], nums[nMin] = nums[nMin], nums[i]


if __name__ == '__main__':
    nums1 = [5,4,3,2,1]
    SelectSort(nums1)
    print(nums1)