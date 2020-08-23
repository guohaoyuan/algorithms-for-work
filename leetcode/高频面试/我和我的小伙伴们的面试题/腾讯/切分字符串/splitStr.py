"""
给定一个任意字符串如123456789,向其中插入一个+加号和=等号
组成123+456=789这样的灯饰，现给定任意字符串，要求一个成立的等式。没有则返回空

"""

class Solution:

    def splitStr(self, s):

        if len(s) <= 2:
            return []
        for i in range(1, len(s)):
            for j in range(i+1, len(s)):
                left = int(s[:i])
                right = int(s[i:j])
                target = int(s[j:])
                tmp = left+right
                if target == tmp:
                    return [s[:i], s[i:j], s[j:]]
        return []

    def splitStrV2(self, s):
        if len(s) <= 2:
            return []
        hashmap = {}

        for i in range(len(s)):
            if s[i:] not in hashmap and len(s[i:]) <= len(s) - 2:
                hashmap[s[i:]] = s[:i]
        print(hashmap)
        # for i in range(1, len(s)):
        #     left = int(s[:i])
        #     target = hashmap


        return []


if __name__ == '__main__':
    s1 = "112233"
    s2 = "123"
    s3 = "111"
    solution = Solution()
    print(solution.splitStrV2(s1))
    # print(solution.splitStrV2(s2))
    # print(solution.splitStrV2(s3))