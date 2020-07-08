# -*- coding = utf-8 -*-

def merge_array(a, l, mid, r, tmp):
    """
    将两个数组合并
    :param a: 原始数组
    :param l: 左指针
    :param mid: 中间指针
    :param r: 右指针
    :param tmp: 临时数组
    :return: None
    """
    i = l
    m = mid
    j = mid + 1
    n = r
    k = 0   # 用于计数将原始数组元素填充到tmp
    # print(n, m)

    while i <= m and j <= n:        # 此处注意两个都要满足
        if a[i] <= a[j]:
            tmp[k] = a[i]
            k += 1
            i += 1
        else:
            tmp[k] = a[j]
            k += 1
            j += 1

    # 如果上面的排序过程结束，但是两个数组其中一个仍然不为空；需要把不为空的数组依次填到tmp中
    while i <= m:
        tmp[k] = a[i]
        k += 1
        i += 1

    while j <= n:
        tmp[k] = a[j]
        k += 1
        j += 1

    # 至此，两个数组均为空，我们需要把辅助数组tmp中的元素挨个填到原始数组中;由于开始位置不一定是整个数组的第一位，所以加上first
    for i in range(k):
        a[l + i] = tmp[i]




def merge_sort(a, first, last, tmp):

    # 算法流程：递归合并：首先将数组递归至左有序，右有序；然后合并左右两个有序序列
    if first < last:
        mid = (first + last) >> 1
        merge_sort(a, first, mid, tmp)
        merge_sort(a, mid + 1, last, tmp)
        merge_array(a, first, mid, last, tmp)

def Merge_sort(a):
    """
    先递归再合并，归并排序
    :param a:
    :return:
    """
    if not a:
        return a

    n = len(a)
    l = 0
    r = n - 1
    tmp = [0 for _ in range(n)]

    merge_sort(a, l, r, tmp)

if __name__ == '__main__':
    test1 = [5, 4, 3, 2, 1]
    Merge_sort(test1)
    print(test1)

# -*- coding: UTF-8 -*-
# class Merge(object):
#     def merge_array(self, a, first, mid, last, tmp):
#         # 1. 初始化变量：目的是将数组a分成两段i:m和j:n；
#         # tmp是个空数组用于存储排序后的结果
#         i = first  #
#         j = mid + 1
#         m = mid
#         n = last
#         k = 0
#
#         # 2. 算法流程：在前后两段中，从各自第一位开始比较大小;将较小的数存储到tmp中，同时tmp和较小数所在指针后移
#         while i <= m and j <= n:
#             if a[i] <= a[j]:
#                 tmp[k] = a[i]
#                 k += 1
#                 i += 1
#             else:
#                 tmp[k] = a[j]
#                 k += 1
#                 j += 1
#
#         # 如果上面的排序过程结束，但是两个数组其中一个仍然不为空；需要把不为空的数组依次填到tmp中
#         while i <= m:
#             tmp[k] = a[i]
#             k += 1
#             i += 1
#
#         while j <= n:
#             tmp[k] = a[j]
#             k += 1
#             j += 1
#
#         # 至此，两个数组均为空，我们需要把辅助数组tmp中的元素挨个填到原始数组中;由于开始位置不一定是整个数组的第一位，所以加上first
#         for i in range(k):
#             a[first + i] = tmp[i]
#         print(a, tmp)
#
#     def merge_sort(self, a, first, last, tmp):
#         # 算法流程：递归合并：首先将数组递归至左有序，右有序；然后合并左右两个有序序列
#         if first < last:
#             mid = (first + last) >> 1
#             self.merge_sort(a, first, mid, tmp)
#             self.merge_sort(a, mid + 1, last, tmp)
#             self.merge_array(a, first, mid, last, tmp)
#
#     def Merge_Sort(self, a):
#         # 1. 考虑特殊情况，数组为空
#         # if not a:
#         #     return 'None'
#
#         # 2. 初始化变量:创建辅助数组tmp
#         n = len(a)
#         tmp = [0] * n
#
#         # 3. 算法流程
#         self.merge_sort(a, 0, n - 1, tmp)
#
#
#
# nums = [3, 1, 10, 5, 9, 6, 4]
# print(nums)
# Merge().Merge_Sort(nums)
# print(nums)