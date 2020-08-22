"""
我们以input:   1   2   3   6   5   4   为例做一个分析

我们存储哈希表中key: value  。key代表当前元素;value代表当前元素为边界的最长序列的长度
    输入1         建立1|1

    输入2         建立1|1+1   2|1+1
        因为1和2相邻所以边界处的序列长度+1
    输入3         建立1|2+1   2|2   3|2+1
        因为3与2相邻，所以3对应的value为hashmap[2]+1;同时更新hashmap[1]+1。
            说白了就是更新边界;此时由于key=2已经在中间了 ，不是边界所以hashmap[2]=无所谓
    输入6         建立1|3     2|2   3|3 断开  6|1
    输入5         建立1|3     2|2   3|3 断开  5|1+1   6|1+1
    输入4         建立1|3+2+1    2|2   3|3 (连接) 4|2+3+1   5|2   6|2+3+1


#####
我们存储哈希表中key: value  。key代表当前元素;value代表当前元素为边界的最长序列的长度
    输入1         建立1|1

    输入2         建立1|1+1   2|1+1
        因为1和2相邻所以边界处的序列长度+1
    输入3         建立1|2+1   2|2+1   3|2+1
        因为3与2相邻，所以3对应的value为hashmap[2]+1;同时更新hashmap[1]+1。
            说白了就是更新边界;此时由于key=2已经在中间了 ，不是边界所以hashmap[2]=无所谓
    输入6         建立1|3     2|3   3|3 断开  6|1
    输入5         建立1|3     2|3   3|3 断开  5|1+1   6|1+1
    输入4         建立1|3+2+1    2|3   3|3 (连接) 4|2+3+1   5|2   6|2+3+1
"""

import collections


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        hashmap = collections.defaultdict(int)
        max_len = 0
        for num in nums:
            if num in hashmap:
                continue
            else:
                # 不再哈希表中
                # 看作边界是否存在
                l = hashmap.get(num - 1, 0)
                r = hashmap.get(num + 1, 0) # 否则会提前出现不该出现的key:value

                # 当前位置的长度
                cur_len = l + r + 1

                if cur_len > max_len:
                    max_len = cur_len

                hashmap[num] = cur_len
                hashmap[num - l] = cur_len
                hashmap[num + r] = cur_len
        return max_len