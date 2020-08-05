"""
合并区间，

步骤：

    1. 特殊情况：数组为空，直接返回空列表
    2. 建立一个结果数组res用于存储结果
    3. 需要对数组进行排序，按照第一个值
    4. 遍历数组，
        如果res为空或者res中最后一个的第二个值<当前区间的第一个值：
            直接加入到res中
        否则：
            更新res最后一个的第二个值，max(res[-1][1], interval[1])
    5. 返回结果
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        # 排序,按照第一个值进行排序
        intervals.sort(key=lambda x: x[0])
        res = []

        # 开始遍历数组
        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                # res[-1][1] > interval[0]表明有交集
                res[-1][1] = max(res[-1][1], interval[1])
        return res