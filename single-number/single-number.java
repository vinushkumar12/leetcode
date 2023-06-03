class Solution {
    public int singleNumber(int[] nums) {
        int temp = 0;
        int counter = 0;
        for (int i = 0; i < nums.length; i++) {
            temp = nums[i];
            for (int b = 0; b < nums.length; b++) {
                if (temp == nums[b])  {
                   counter++; 
                }
            }
            if (counter == 1) {
                break;
            }
            counter = 0;
        }
        return temp;
    }
}