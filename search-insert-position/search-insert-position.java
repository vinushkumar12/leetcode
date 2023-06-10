class Solution {
    public int searchInsert(int[] nums, int target) {
       int start = 0;
       int end = nums.length - 1;
       int possible = 0;
       if (nums[0] > target) {
           return 0;
       } else if (nums[end] < target) {
           return end + 1;
       }
       while (start <= end) {
           int middle = start + (end - start)/2;
           if (nums[middle] == target) {
               return middle;
           } else if (nums[middle] < target) {
               start = middle + 1;
               int diff1 = target - nums[middle];
               int diff2 = target - nums[possible];
               if (diff2 < 0) {
                   diff2 = -diff2;
               }
               if (diff2 >= diff1) {
                   possible = middle + 1;
               }
           } else if (nums[middle] > target) {
               end = middle - 1;
               int diff1 = nums[middle] - target;
               int diff2 = nums[possible] - target;
               if (diff2 < 0) {
                   diff2 = -diff2;
               }
               if (diff2 >= diff1) {
                   possible = middle;
               }               
           }
           System.out.println("start " + start);
           System.out.println("end " + end);
           System.out.println("middle " + middle);
           System.out.println("possible " + possible);
           
       }
       return possible; 
    }
}