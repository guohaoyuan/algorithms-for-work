class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n1 = len(a)
        n2 = len(b)
        # 特殊情况
        if not a:
            return b
        if not b:
            return a

        # 表示进位符号
        tmp = 0
        # 存储结果
        res = ""
        # 相加和
        while n1 and n2:
            # 两数之和加上进位符
            sum_ = int(a[-1]) + int(b[-1]) + int(tmp)
            shang, yu = sum_ // 2, sum_ % 2
            res += str(yu)
            # 更新字符串和进位符
            tmp = shang
            a, b = a[:-1], b[:-1]
            n1 -= 1
            n2 -= 1
        while n1:
            sum_ = int(a[-1]) + tmp
            shang, yu = sum_ // 2, sum_ % 2
            res += str(yu)
            tmp = shang
            a = a[:-1]
            n1 -= 1
        while n2:
            sum_ = int(b[-1]) + tmp
            shang, yu = sum_ // 2, sum_ % 2
            res += str(yu)
            tmp = shang
            b = b[:-1]
            n2 -=1
        if tmp:
            res += str(1)
        return res[::-1]