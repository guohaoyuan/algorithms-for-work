"""
创建一个栈，一个哈希表（哈希表中存放左括号：右括号）

1. 特殊情况：如果字符串为空。直接返回True
2. 遍历字符串s:
        如果当前栈stack为空，或者当前字符是右括号，直接入栈
        如果当前栈存在：
            如果当前栈顶元素==哈希表中对应的左括号：右括号，表示匹配上了，还需要pop栈顶元素
            否则，表示没有匹配上，直接返回False
3. 如果上面的遍历操作结束，stack依旧存在，返回False;否则返回True
"""
class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True

        hashmap = {')': "(", "]": "[", "}": "{"}
        stack = []

        for key in s:
            if not stack or key not in hashmap:
                stack.append(key)
            if key in hashmap:
                if stack[-1] == hashmap[key]:
                    stack.pop()
                else:
                    return False
        return not stack

if __name__ == '__main__':
    s = "()"
    solution = Solution()
    tmp = solution.isValid(s)
    print(tmp)