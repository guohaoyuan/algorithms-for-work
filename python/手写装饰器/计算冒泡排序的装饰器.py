import time

def out(fuc):
    def inner(*args):
        start = time.time()
        fuc(*args)
        end = time.time()
        print("custom time is %f" % (end - start))
    return inner

@out
def Bubble1(nums):
    if not nums:
        return nums

    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
@out
def Bubble2(nums):
    if not nums:
        return nums

    n = len(nums)

    for i in range(n):
        flag = False
        for j in range(i + 1, n):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                flag = True
        if not flag:
            break

if __name__ == "__main__":
    test1 = [5, 4, 3, 2, 1]
    Bubble1(test1)
    Bubble2(test1)
    print(test1)

    test2 = [1, 2, 3, 4, 5]
    Bubble1(test2)
    Bubble2(test2)
    print((test2))