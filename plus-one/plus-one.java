class Solution {
    public int[] plusOne(int[] digits) {
        if (digits[digits.length - 1] != 9) {
           digits[digits.length - 1] = digits[digits.length - 1] + 1;
           return digits;
       } else {
           int num_nines = 0;
           for (int i = digits.length - 1; i >= 0; i--) {
               if (digits[i] == 9) {
                   num_nines++;
               } else {
                   break;
               }
           }
           if (num_nines == digits.length) {
               int [] ans = new int[num_nines + 1];
               ans[0] = 1;
               for (int i = 1; i < ans.length; i++) {
                   ans[i] = 0;
               }
               return ans;
           } else {
               int [] ans = new int[digits.length];
               for (int i = digits.length - 1; i >= 0; i--) {
                   if (digits[i] == 9) {
                       ans[i] = 0;
                   } else {
                       ans[i] = digits[i] + 1;
                       for (int x = i - 1; x >= 0; x--) {
                           ans[x] = digits[x];
                       }
                       return ans;
                   }
               }
           }
       }
       return null;
    }
}