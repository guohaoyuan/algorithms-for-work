package test;

import java.util.Arrays;

public class nextPermutation {
    public static void method(int[] nums) {
        int n = nums.length;
        for (int i = n-2; i>=0; i--) {
            if (nums[i] < nums[i+1]) {
                int index = i;
                Arrays.sort(nums, index + 1, n);
                for (int j = index + 1; j < n; j++) {
                    if (nums[j] > nums[index]) {
                        System.out.println("j="+j+", index="+index);
                        int tmp = nums[j];
                        nums[j] = nums[index];
                        nums[index] = tmp;
                        return ;
                    }
                }
            } else if (i==0) {
                Arrays.sort(nums);
                return ;

            }
        }
    }

    public static void main(String[] args) {
        int[] nums = new int[]{1, 2};
        method(nums);
        for (int i = 0; i < nums.length; i++) {

            System.out.print(nums[i] + ",");
        }
    }
}
