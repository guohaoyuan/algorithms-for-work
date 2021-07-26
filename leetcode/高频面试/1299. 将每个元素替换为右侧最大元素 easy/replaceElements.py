"""
步骤：
    1. 特殊情况：数组为空，则直接返回[]；数组长度为1，则直接返回[-1]
    2. 初始化结果res=[0]*(n-1) + [-1]，n表示数组长度
    3. 逆序遍历原数组，注意起始位置为n-2，终止位置0
        在这个过程，选择原数组和结果数组中较大的数
        举例：
             arr = [17,18,5,4,6,1]
             res = [0, 0,0,0,0,-1]
    4. 返回res
"""


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if not arr:
            return []
  
        if n == 1:
            return [-1]
        
        n = len(arr)
        res = [0] * n
        res[-1] = -1
        
        # for i in range(n-1):
        #     res[i] = max(arr[i + 1:])
        # return res
        for i in range(n - 2, -1, -1):
            res[i] = max(res[i + 1], arr[i + 1])
        return res

"""
做优化
"""
class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        # 1. 特殊情况：数组长度为0或者1
        n = len(arr)
        if n == 0:
            return []
        elif n == 1:
            return [-1]
        
        # 2. 初始化返回结果res
        res = [0] * n
        res[-1] = -1 

        # 3. 倒数第二位遍历数组，并更新res
        for i in range(n - 2, -1, -1):
            res[i] = max(res[i + 1], arr[i + 1])
        
        return res
