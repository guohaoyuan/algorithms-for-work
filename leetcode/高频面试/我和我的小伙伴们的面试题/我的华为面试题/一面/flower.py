class Solution:
    def flower(self, num):

        tmp = num
        res = 0
        while True:
            shang, yu = num // 10, num % 10
            res += yu*yu*yu
            # print(res)
            num = shang
            if shang == 0:
                break
        if res == tmp:
            return True
        else:
            return False

if __name__ == '__main__':
    solution = Solution()
    res = []
    for i in range(100, 1000):
        if solution.flower(i):
            res.append(i)
        else:
            continue
    print(res)
    print(solution.flower(153))