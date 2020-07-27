"""
步骤：
    1. 特殊情况：数组为空，则直接返回·[]
    2. 初始化结果res=[0]*(n-1) + [-1]
    3. 逆序遍历原数组，注意起始位置为n-2，终止位置0
        在这个过程，选择原数组和结果数组中较大的数
    4. 返回res
"""

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if not arr:
            return []
        n = len(arr)
        res = [0] * (n - 1) + [-1]

        for i in range(n-2, -1, -1):
            res[i] = max(res[i + 1], arr[i + 1])
        return res