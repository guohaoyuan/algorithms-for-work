import sys

input_data = sys.stdin.readline().split()
nums = [int(x) for x in input_data]

def helper(num):
    res = 0
    # 特殊情况：输入为0
    while True:
        shang, yu = num // 10, num % 10
        res += yu
        num = shang
        if shang == 0:
            break
    return res


print(helper(nums[0]), helper(nums[1]))
print(helper(nums[0]) % helper(nums[1]))