class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        int [] answer = new int [2];
        int index = 0;
       
        
        for(int i = 0; i < nums.length; i++)
        {
            index++;
            for(int b = index; b < nums.length; b++)
            {
                if(nums[i] + nums[b] == target)
                {
                    answer[0] = i;
                    answer[1] = b;
                    return answer;
                }
            }
        }
        return answer;
        
    }
}
