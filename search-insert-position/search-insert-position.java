class Solution {
    public int searchInsert(int[] nums, int target) {
       int start = 0;
       int end = nums.length - 1;
       int possible = 0;
       while (start <= end) {
           int middle = start + (end - start)/2;
           if (nums[middle] == target) {
               return middle;
           } else if (nums[middle] < target) {
               start = middle + 1;
               int diff2 = target - nums[possible];
               if (diff2 < 0) {
                   diff2 = -diff2;
               }
               if (diff2 >= target - nums[middle] ) {
                   possible = middle + 1;
               }
           } else if (nums[middle] > target) {
               end = middle - 1;
               int diff2 = nums[possible] - target;
               if (diff2 < 0) {
                   diff2 = -diff2;
               }
               if (diff2 >= nums[middle] - target) {
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