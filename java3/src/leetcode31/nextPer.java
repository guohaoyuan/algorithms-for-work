package leetcode31;

import java.util.Arrays;

class nextPer {
    public static void nextA(int[] nums) {
        int index;
        int n = nums.length;
        for (int i = n - 2; i >= 0; i--) {
            if (nums[i] < nums[i+1]) {
                index = i;
                Arrays.sort(nums, index + 1, n);
                for (int j = index + 1; j < n; j++){
                    if (nums[j] > nums[index]) {
                        int tmp = nums[j];
                        nums[j] = nums[index];
                        nums[index] = tmp;
                        return;
                    }
                }
            } else if (i == 0) {
                Arrays.sort(nums);
                return;
            }
        }
    }

    public static void main(String[] args) {
        int[] nums = {1, 2, 3};
        nextA(nums);
        for (int i = 0; i < nums.length; i++) {
            System.out.print(nums[i] + ", ");
        }
    }
}
