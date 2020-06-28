"""
1. 从左上角开始,
    遇到小于当前值的, 左移
    遇到大于当前值的, 下移
"""
class Solution:
    def searchMatrix(self, matrix, target):
        # 1. 特殊情况:数组为空
        if not matrix:
            return False

        # 2. 初始化矩阵的行 列
        m = len(matrix) - 1
        n = len(matrix[0]) - 1
        r = 0
        c = n

        # 3. 算法流程,按照上面的要求来
        while r <= m and c >= 0:
            if matrix[r][c] > target:
                c -= 1
            elif matrix[r][c] < target:
                r += 1
            elif matrix[r][c] == target:
                return True
        # 遍历结束也没找到,
        return False


if __name__ == '__main__':
    nums1 = [ [1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30] ]
    target1 = 5
    target2 = 20
    solution = Solution()
    print(solution.searchMatrix(nums1, target1))
    print(solution.searchMatrix(nums1, target2))
    """
    时间复杂度: m + n
    空间复杂度: 1
    """