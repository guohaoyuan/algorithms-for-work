"""
按照三数之和去做
"""

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 1. 初始化长度和排除长度不足2的情况
        n = len(numbers)
        if n < 2:
            return []
        
        # 不用排序了,已经是升序了

        # 2. 遍历数组nums，并初始化元素a
        for i in range(n):
            a = numbers[i]

            # 3. 排除重复元素
            if i > 0 and numbers[i] == numbers[i-1]:
                continue

            # 4. 利用双指针进行遍历
            j = n - 1
            while i < j:
                b = numbers[j]
                sum_ = a + b

                if sum_ == target:
                    # 直接返回结果了
                    return [i + 1, j + 1]
                    # res.append([i + 1, j + 1])
                    # 5. 更新b
                    # while numbers[j] == numbers[j+1]:
                    #     j -= 1
                    # j -= 1
                    
                elif sum_ > target:
                    j -= 1
                else:
                    i += 1
