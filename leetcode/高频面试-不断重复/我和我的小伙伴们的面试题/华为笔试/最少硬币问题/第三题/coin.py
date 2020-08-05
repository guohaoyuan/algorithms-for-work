"""

"""
import sys

# input_data = []
# data = []

# for line in sys.stdin:
#     input_data = line.split()
#     data.append([int(x) for x in input_data])

input_data = sys.stdin.readline().split()

data = [int(x) for x in input_data]

print(data[0], data[1:])
def helper(amount, coins):
    if amount == 0:
        return 1
    if not coins:
        return 0

    # 初始化dp
    n = len(coins)
    # dp = [[0 for _ in range(amount + 1)] for _ in range(n + 1)]
    dp = [0 for _ in range(amount + 1)]
    # for i in range(n + 1):
    # dp[i][0] = 1

    dp[0] = 1

    for i in range(1, len(coins) + 1):
        for j in range(1, amount + 1):
            if j - coins[i - 1] >= 0:
                # dp[i][j] = dp[i][j - coins[i-1]] + dp[i-1][j]
                dp[j] = dp[j - coins[i - 1]] + dp[j]
            else:
                # dp[i][j] = dp[i-1][j]
                dp[j] = dp[j]
    return dp[-1]

print(helper(data[0], data[1:]))