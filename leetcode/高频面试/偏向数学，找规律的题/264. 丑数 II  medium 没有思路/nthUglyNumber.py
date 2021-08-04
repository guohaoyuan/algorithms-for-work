"""
第一个丑数是1
可以看出丑数是1，2,3,5相乘得到，每次就利用当前位置的丑数找到下一个位置丑数
利用p2 p3 p5 三个指针均是从0开始，分别乘2 3 5,寻找最小的的丑数，补充到res中。
哪个丑数被用到了，就哪个指针+=1
一直到遍历n次
"""

class Solution(object):

    def generate_ugly(self, res, n):
        if n == 1:
            return res[0]

        res = [1] * n
        p2 = 0
        p3 = 0
        p5 = 0

        for i in range(1, n):
            temp_res_p2 = res[p2] * 2
            temp_res_p3 = res[p3] * 3
            temp_res_p5 = res[p5] * 5

            min_ugly = min(temp_res_p2, temp_res_p3, temp_res_p5)

            res[i] = min_ugly

            if min_ugly == temp_res_p2:
                p2 += 1
            if min_ugly == temp_res_p3:
                p3 += 1
            if min_ugly == temp_res_p5:
                p5 += 1
        return res[n - 1]
    
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [1]

        return self.generate_ugly(res, n)
