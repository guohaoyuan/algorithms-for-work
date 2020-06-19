class Solution:

    def letterCombinations(self, digits):
        # 1. 特殊情况: 字符串为空,返回空列表
        if not digits:
            return []

        # 2. 初始化路径 返回结果
        path = []
        res = []
        n = len(digits)
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

        # 3. 算法流程
        def back_track(path, nextdigit):
            # 递归结束条件,字符串长度为输入长度
            if len(path) == n:
                res.append(''.join(path[:]))
                return
            # 在选择列表中做选择
            # 与之前全排列的区别在于,输入为字符串而不是list所以,是截断
            for letter in phone[nextdigit[0]]:  # 得到当前截取字符串的第一个数字
                path.append(letter)
                back_track(path, nextdigit[1:]) # 截取字符串
                path.pop()
        back_track(path, digits)
        return res
    def letterCombinations_v2(self, digits):
        # 1. 特殊情况: 字符串为空,返回空列表
        if not digits:
            return []

        # 2. 初始化路径 返回结果
        path = []
        res = []
        n = len(digits)
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

        # 3. 算法流程
        def back_track(path, nextdigit, start):
            # 递归结束条件,字符串长度为输入长度
            if len(path) == n:
                res.append(''.join(path[:]))
                return
            # 在选择列表中做选择
            # 与之前全排列的区别在于,输入为字符串而不是list所以,是截断
            for letter in phone[nextdigit[start]]:  # 得到当前截取字符串的第一个数字
                path.append(letter)
                back_track(path, nextdigit, start + 1) # 截取字符串
                path.pop()
        back_track(path, digits, 0)
        return res
if __name__ == "__main__":
    digits1 = "23"
    solution = Solution()
    print(solution.letterCombinations_v2(digits1))
    """
    时间复杂度: 3^n1 * 4^(n-n1), n1表示按键有三种取值,n2表示按键有四种取值
    时间复杂度: 一样
    """