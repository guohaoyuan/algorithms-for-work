import sys

input_data = sys.stdin.readline().split()
nums = [int(x) for x in input_data]

def helper(num):
    # 特殊情况：输入为0
    if num == 0:
        return 0

    # 计算商和余数
    shang, yu = num // 10, num % 10
    res = 0

    while shang:
        res += yu
        num = shang
        shang, yu = num // 10, num % 10
    res += yu
    return res


print(helper(nums[0]), helper(nums[1]))
print(helper(nums[0]) % helper(nums[1]))