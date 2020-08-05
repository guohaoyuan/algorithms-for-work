"""
公司为加班员工提供自选食物，每个员工加班后可以自选X元物品，
夜宵提供上有价格1元，3元，7元，11元，13元的商品个A，B，C，D，E件;
如果选择X元商品，那么最少需要选取多少件呢？（至少存在一种商品的选择方案）

测试样例
A,B,C,D,E=1,2,3,4,5
X=30

output:
4
"""

"""
第一种方法：贪心策略

要保证硬币数目尽可能小，我们从高往低选；
选择过程取[理想可选硬币数，实际能选硬币数]中最小的那一个
然后更新目标X

时间复杂度：1.硬币面值个数也就是5
空间复杂度：1
"""

"""
https://www.cnblogs.com/lepeCoder/p/NOJ-1221.html

第二种方法：动态规划

1.定义状态:
        dp[k]表示目标为k时候的最少硬币数

2. base case:
        dp[0] = 0 目标为零是最少硬币数0
        dp[1:] = amount + 1 表示正无穷，一个无法取到的值

3. 转移方程:
        dp[i] = min(dp[i], dp[i - coin] + 1) if i - coin >= 0
                continue                     otherwise   
"""

class Solution:

    def coinChange(self, coins, coins_num, amount):
        """

        :param coins: 硬币面值[1, 3, 7, 11, 13]
        :param coins_num: 硬币数目[1, 2, 3, 4, 5]
        :param amount: 拼凑的目标30
        :return: 所需最少硬币数
        """
        # 因为题干已经说明，输入均为正常值

        # 初始化返回结果
        res = 0

        # 在循环中，从高到低拼凑硬币
        for i in range(len(coins) - 1, -1, -1):
            # tmp 临时存储当前能取到的硬币数
            tmp = min(coins_num[i], amount // coins[i])
            # 更新当前目标
            amount -= tmp * coins[i]
            # 当前硬币数
            res += tmp

            # 找到目标直接退出
            if amount == 0:
                break
        return res

    def coinChange_v2(self, coins, coins_num, amount):
        # 1, 初始化数组
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        # 2. 动态转移有三层，第一层是遍历不同面值硬币
        #                  第二层是遍历不同数目的硬币数
        #                   第三层从前向后遍历dp数组
        for i in range(len(coins)):
            for j in range(1, coins_num[i] + 1):
                for k in range(1, amount + 1):
                    if k - coins[i] < 0:
                        continue
                    dp[k] = min(dp[k], dp[k - coins[i]] + 1)
        return dp[-1] if dp[-1] != amount + 1 else -1


if __name__ == '__main__':
    coins = [1, 3, 7, 11, 13]
    coins_num = [1, 2, 3, 4, 1]
    amount = 30
    solution = Solution()
    print(solution.coinChange(coins, coins_num, amount))
    print(solution.coinChange_v2(coins, coins_num, amount))