我们首先找到一个上升，index1
然后index1后面先进行升序，然后找到第一个大于index1的数，交换位置

class Solution {
    public void nextPermutation(int[] nums) {
        int n = nums.length;
        if (n==1) {
            return ;
        }
        int index;
        // 找到第一个上升序列
        for (int i = n - 2; i >=0; i--) {
            if (nums[i] < nums[i + 1]) {
                index = i;
                Arrays.sort(nums, index + 1, n); // n不参与排序
                for (int j = index + 1; j < n; j++) {
                    if (nums[j] > nums[index]) {
                        int tmp = nums[index];
                        nums[index] = nums[j];
                        nums[j] = tmp;
                        return ;
                    }
                }
            } else if (i == 0) {
                // 这里很有技巧，表示原序列是降序
                Arrays.sort(nums);
                return ;
            }
        }
        // 我们先把index后面的升序排列


    }
}