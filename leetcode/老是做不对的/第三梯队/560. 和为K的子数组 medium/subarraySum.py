# public class Solution {
#     public int subarraySum(int[] nums, int k) {
#         int count = 0;
#         for (int start = 0; start < nums.length; ++start) {
#             int sum = 0;
#             for (int end = start; end >= 0; --end) {
#                 sum += nums[end];
#                 if (sum == k) {
#                     count++;
#                 }
#             }
#         }
#         return count;
#     }
# }
#
#
#
# class Solution {
#     public int subarraySum(int[] nums, int k) {
#         int count = 0;
#         for (int i = 0; i < nums.length; i++) {
#             int tmp = k;
#             for (int j = i; j < nums.length; j++ ) {
#                 tmp = tmp - nums[j];
#                 if (tmp == 0) {
#                     count++;
#                 }
#             }
#         }
#         return count;
#     }
# }

"""
说实话有点像leetcode 1
前缀和+哈希表;时间换空间，能够将时间复杂度从n^2降到n

1. 首先建立一个哈希表hashmap;初始化一个值0:1;count计数器;pre前缀和=0
比如
    nums:   3   4   7   2   -3  1   4   2
    pre:0   3   7   14  16  13  14  18  20
    pre-2:  1   5   12  14  11  12  16  18
2. 遍历数组nums,如果当前nums[i]-k存在于hashmap中，则count+=hashmap[pre-2]
    否则，向哈希表中添加新值或者加1.可以利用defaultdict(int)
3. 最后返回count
"""

import collections
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = collections.defaultdict(int)
        hashmap[0] = 1
        count = 0
        pre = 0
        for i in range(len(nums)):
            pre += nums[i]
            tmp = pre - k
            if tmp in hashmap:
                count += hashmap[tmp]
            hashmap[pre] += 1
        return count

"""
做了自适应
"""


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 初始化哈希表
        hashmap = {0: 1}
        count = 0  # 计数器
        sum_ = 0  # 前缀和

        # 遍历数组
        for num in nums:
            # 更新前缀和
            sum_ += num

            # 判断当前前缀和是否值得计数器计数
            # 这一步必须在更新哈希表前进行
            tmp = sum_ - k
            if tmp in hashmap:
                count += hashmap[tmp]

            # 更新哈希表
            if sum_ not in hashmap:
                hashmap[sum_] = 1
            else:
                hashmap[sum_] += 1
        return count