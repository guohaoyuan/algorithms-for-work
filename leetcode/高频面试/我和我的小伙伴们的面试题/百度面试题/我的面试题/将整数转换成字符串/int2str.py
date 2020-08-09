"""
我是真的菜
将整型转换成字符串，
例如，
    1->A, 2->B, 3->C
    4->AA 5->AB 6->AC
    7->BA 8->BB 9->BC
    10->CA 11->CB 12->CC
    13->AAA 14->AAB 15->AAC
"""

class Solution:
    def int2str(self, n):
        """

        :param n: > 0
        :return: str
        """
        shang, yu = n // 3, n % 3
        res = ''

        while True:
            if shang:
                if yu == 0:
                    res += 'C'
                    shang -= 1
                if yu == 1:
                    res += "A"
                if yu == 2:
                    res += "B"
                # 更新商和余数
                shang, yu = shang // 3, shang % 3
            else:
                # 此时余数还存在
                if yu == 0:
                    res += "C"
                if yu == 1:
                    res += "A"
                if yu == 2:
                    res += "B"
                break
        res = res[::-1]
        return res
def num2str(num):
    res = ""
    while True:
        shang, yu = num // 3, num % 3
        if yu == 1:
            res += 'a'
        elif yu == 2:
            res += 'b'
        elif yu == 0:
            res += 'c'
            shang = shang - 1
        num = shang
        if shang == 0:
            return res[::-1]
if __name__ == '__main__':
    test1 = 18
    solution = Solution()
    print(solution.int2str(test1))
    print(num2str(test1))