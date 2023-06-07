class Solution {
    public int findNumbers(int[] nums) {
        int counter = 0;
        for(int i = 0; i < nums.length; i++) {
            int x = String.valueOf(nums[i]).length();
            if(x % 2 == 0) {
                counter++;
            }
        }
        return counter;
    }
}