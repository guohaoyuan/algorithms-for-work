"""
除了1和它本身以外不再有其他因数的数称为质数
"""
res = []

for i in range(3, 101):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        res.append(i)
print(res)
res.extend([1, 2])
print(res)