class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # 1. 初始化两个字符串的长度n1 n2;两个字符串的指针p1, p2,；进位符号tmp
        n1, n2 = len(a), len(b)
        p1, p2 = n1 - 1, n2 - 1
        tmp = 0
        res = ""
        sum_ = 0

        # 2. 从后往前一次相加
        while p1 >= 0 and p2 >= 0:
            sum_ = int(a[p1]) + int(b[p2]) + tmp
            shang, yu = sum_ // 2, sum_ % 2

            # 更新结果res和进位符号
            res += str(yu)
            tmp = shang

            # 更新两个指针
            p1 -= 1
            p2 -= 1
        
        while p1 >= 0:
            sum_ = int(a[p1]) + tmp
            shang, yu = sum_ // 2, sum_ % 2

            res += str(yu)
            tmp = shang

            p1 -= 1
            
        while p2 >= 0:
            sum_ = int(b[p2]) + tmp
            shang, yu = sum_ //2, sum_ % 2

            res += str(yu)
            tmp = shang

            p2 -= 1
        
        # 3. 对最后的进位符号进行处理
        if tmp > 0:
            res += str(tmp)
        res = res[::-1]
        return res
