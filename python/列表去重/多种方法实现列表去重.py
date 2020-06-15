# -*- coding : utf-8 -*-


# 利用集合去重
l1 = [1, 2, 3, 1, 2, 3]
l2 = list(set(l1))
print(l2)

# 利用集合并保持顺序
l1 = [1, 2, 3, 1, 2, 3]
l2 = list(set(l1))
l2.sort(key=l1.index)
print(l2)

# 利用字典去重
l1 = [1, 2, 3, 1, 2, 3]
l2 = {}.fromkeys(l1).keys()
print(list(l2))

# 利用列表推导
l1 = [1, 2, 3, 1, 2, 3]
l2 = []
[l2.append(x) for x in l1 if x not in l2]
print(l2)

