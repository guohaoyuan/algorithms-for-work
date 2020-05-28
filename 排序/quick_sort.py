# -*- coding = utf-8 -*-

def partition(l, r, a):
    """
    :param l: 左指针
    :param r: 右指针
    :param a: 传入数组
    :return: 返回索引
    """
    i = l
    j = r
    x = a[l]    # 挖的第一个坑

    while i < j:
        while i < j and a[j] > x:
            j -= 1
        if i < j:
            a[i] = a[j] # 用现在的值覆盖之前的坑
            i += 1

        while i < j and a[i] < x:
            i += 1
        if i < j:
            a[j] = a[i] # 用当前值覆盖之前的坑
            j -= 1


    # 此时i=j
    # 填充最早的坑
    a[i] = x
    return i

def quick_sort(a, l, r):
    """
    首先为第一个元素找一个位置，使得左边的都比他小，右边的都比他大；然后在左右两部分递归。利用分而制之
    :param a:
    :param l:
    :param r:
    :return:
    """
    if l < r:   # 与归并排序类似
        i = partition(l, r, a)
        quick_sort(a, l, i - 1)
        quick_sort(a, i + 1, r)

def Quick_sort(a):
    # 1. 特殊情况：数组为空
    if not a:
        return a

    # 2. 初始化变量
    n = len(a)
    l = 0
    r = n - 1

    # 3. 算法流程
    quick_sort(a, l, r)

if __name__ == "__main__":
    test1 = [5, 4, 3, 1]
    Quick_sort(test1)
    print(test1)