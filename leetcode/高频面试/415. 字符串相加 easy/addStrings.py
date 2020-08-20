class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n1 = len(num1)
        n2 = len(num2)
        tmp = 0  # 进位符
        i = n1 - 1
        j = n2 - 1
        res = ""  # 返回结果

        while i >= 0 and j >= 0:
            sum_ = int(num1[i]) + int(num2[j]) + tmp
            shang, yu = sum_ // 10, sum_ % 10

            # 更新进位符，更新两个指针
            tmp = shang
            i -= 1
            j -= 1
            # 将余数累加
            res += str(yu)

        while i >= 0:
            sum_ = int(num1[i]) + tmp
            shang, yu = sum_ // 10, sum_ % 10

            tmp = shang
            i -= 1
            res += str(yu)

        while j >= 0:
            sum_ = int(num2[j]) + tmp
            shang, yu = sum_ // 10, sum_ % 10

            tmp = shang
            j -= 1
            res += str(yu)

        if tmp == 1:
            res += str(tmp)
        res = res[::-1]
        return res