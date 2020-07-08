
def InsertSort_v2(nums):

    # 1. 特殊情况：数组为空
    n = len(nums)

    if n < 2:
        return nums

    # 2. 插入排序，
    for i in range(1, n):

        for j in range(i - 1, -1, -1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
if __name__ == "__main__":
    num1 = [5, 4, 3, 2, 1]
    InsertSort_v2(num1)
    print(num1)