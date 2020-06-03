# -*- coding = utf-8 -*-

class Solution:

    def getleastNumbers(self, arr, k):
        """
        利用快排的思想，使得index逼近k-1
        :param arr: list数组
        :param k: int整数
        :return: 最小的k个数组成的list
        """

        # 1. 特殊情况：数组为空或k==0
        if not arr or k == 0:
            return []

        # 2. 初始化：左右指针
        L = 0
        R = len(arr) - 1

        # 3. 算法流程
        def partition(arr, L, R):
            i = L
            j = R
            x = arr[L]

            while i < j:
                while i < j and arr[j] > x:
                    j -= 1

                if i < j:
                    arr[i] = arr[j]
                    i += 1

                while i < j and arr[i] < x:
                    i += 1
                if i < j:
                    arr[j] = arr[i]
                    j -= 1

            arr[j] = x
            return j

        index = partition(arr, L, R)
        # print(index)
        while index != k - 1:
            if index < k - 1: # 为了逼近 k-1，收缩左边界
                L = index + 1
                index = partition(arr, L, R)
                # print("a")
            # if index > k - 1: # 为了逼近 k-1，收缩右边界
            else:
                R = index - 1
                index = partition(arr, L, R)
                # print("b")
        return arr[: index + 1]

if __name__ == '__main__':
    test1 = [3, 2, 1]
    k1 = 2
    test2 = [0, 1, 2, 1]
    k2 = 1
    solution = Solution()
    print(solution.getleastNumbers(test1, k1))
    print(solution.getleastNumbers(test2, k2))
    '''
    时间复杂度：n，partition函数：选择一个参考元素，大于参考元素的放在左边小于参考元素的放在右边，故时间复杂度为n
    空间复杂度：1，常数量的变量'''