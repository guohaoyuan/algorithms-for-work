class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        # 行列
        m = len(matrix) - 1
        n = len(matrix[0]) - 1
        i, j = 0, n
        while i <= m and j >= 0:
            print("i = {}, j = {}, matrix[i][j] = {}".format(i, j, matrix[i][j]))
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                # 向下
                i += 1
            elif matrix[i][j] > target:
                j -= 1
        return False

if __name__ == '__main__':
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    solution = Solution()
    print(solution.searchMatrix(matrix, target=5))