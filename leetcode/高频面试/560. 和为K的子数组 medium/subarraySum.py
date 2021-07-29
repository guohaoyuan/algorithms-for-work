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
    pre-k:  1   5   12  14  11  12  16  18
    
计算完包括了当前数前缀和以后，我们去查一查在当前数之前，有多少个前缀和等于 preSum - k 呢？
这是因为满足 preSum - (preSum - k) == k 的区间的个数是我们所关心的

作者：liweiwei1419
链接：https://leetcode-cn.com/problems/subarray-sum-equals-k/solution/bao-li-jie-fa-qian-zhui-he-qian-zhui-he-you-hua-ja/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
2. 遍历数组nums,如果当前nums[i]-k存在于hashmap中，则count+=hashmap[pre-2]
    否则，向哈希表中添加新值或者加1.可以利用defaultdict(int)
3. 最后返回count
"""

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 1. 初始化前缀和字典，一开始还没有遍历数组nums，所以前缀和初始化为0:1
        sum_dict = collections.defaultdict(int)
        sum_dict[0] = 1
        # 初始化返回结果与前缀和
        res = 0
        pre_sum = 0

        # 2. 遍历数组nums，更新前缀和
        for num in nums:
            pre_sum += num
            
            # 如果前缀和-k 在字典中，则说明截断下来的子数组是满足和为k的
            if pre_sum - k in sum_dict:
                # 进行计数
                res += sum_dict[pre_sum - k]
            # 添加前缀和到字典中
            sum_dict[pre_sum] += 1

        return res
