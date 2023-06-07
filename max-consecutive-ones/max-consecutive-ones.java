class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int counter = 0;
        int greatest = 0;
        for(int i = 0; i < nums.length; i++) {
            if(nums[i] == 1) {
                counter++;
            } else {
                if(counter > greatest) {
                    greatest = counter;
                }
                counter = 0;
            }
        }
        if(greatest > counter) {
            return greatest;
        }
        return counter;
        
    }
}