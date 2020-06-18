# -*- coding = utf-8 -*-

def bubble_sort1(a):
    """
    version1在数组有序仍然时间复杂度为n**2women需要改进
    :param a:
    :return:
    """
    if not a:
        return a

    # 2. 初始化
    n = len(a)

    for i in range(n):
        for j in range(i + 1, n):
            if a[i] > a[j]: # 稳定排序，只有严格大于时，才改变位置
                a[i], a[j] = a[j], a[i]


def bubble_sort2(a):
    if not a:
        return a

    # 2
    n = len(a)

    for i in range(n):
        # 开始遍历前先设置一个变量flag来判断是否有序
        flag = True    # T表示数组有序
        for j in range(i + 1, n):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
                flag = False     # 经过判断语句，表述数组需要排序;若是美景过判断表示数组有序，在下面直接跳出

        if flag: # 表示flag已经有序
            break

if __name__ == '__main__':
    test1 = [5, 4, 3, 2, 1]
    bubble_sort1(test1)
    print(test1)
    test2 = [4, 3, 2, 1]
    bubble_sort2(test2)
    print(test2)