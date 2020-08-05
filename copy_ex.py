# -*- coding = utf-8 -*-


# class Animal(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def eat(self):
#         print("%s is eating!" % self.name)
#
# class Person(Animal):
#     def __init__(self, name, age, sex):
#         super(Person, self).__init__(name, age)
#         self.sex = sex
#
#     def eat(self):
#         super(Person, self).eat()
#         print("person is eating!")
#
# person = Person("ghy", 35, "nan")
# person.eat()

# import sys
#
# input_data = []
# data = []
#
# for line in sys.stdin:
#     input_data = line.split()
#     data.append([int(x) for x in input_data])
# print(data)
#
# def helper(target, nums, coins):
#     res = 0
#
#     for i in range(len(nums) - 1, -1, -1):
#         need = min(target//coins[i], nums[i])
#         target = target - need*coins[i]
#         res += need
#         if target == 0:
#             return res
#
# print(helper(data[1], data[0], [1, 3, 7, 11, 13]))


class Solution:
    def addBinary(self, a, b):
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
            print("a=", a, "b=", b)
            n1 -= 1
            n2 -= 1
            print("n1 ={}, n2 = {}".format(n1, n2))
        while n1:
            sum_ = int(a[-1]) + tmp
            shang, yu = sum_ // 2, sum_ % 2
            res += str(yu)
            tmp = shang
            a = a[:-1]
            n1 -= 1
        while n2:
            print("b =", b)
            sum_ = int(b[-1]) + tmp
            shang, yu = sum_ // 2, sum_ % 2
            res += str(yu)
            tmp = shang
            b = b[:-1]
            n2 -= 1
        if tmp:
            res += str(1)
        return res[::-1]
if __name__ == '__main__':
    a = "100"
    b = "110010"
    solution = Solution()
    print(solution.addBinary(a, b))