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

import sys

input_data = []
data = []

for line in sys.stdin:
    input_data = line.split()
    data.append([int(x) for x in input_data])
print(data)

def helper(target, nums, coins):
    res = 0

    for i in range(len(nums) - 1, -1, -1):
        need = min(target//coins[i], nums[i])
        target = target - need*coins[i]
        res += need
        if target == 0:
            return res

print(helper(data[1], data[0], [1, 3, 7, 11, 13]))