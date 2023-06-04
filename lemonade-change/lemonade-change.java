class Solution {
    public boolean lemonadeChange(int[] bills) {
       int num_5 = 0;
       int num_10 = 0;
       for (int i = 0; i < bills.length; i++) {
           if ((bills[i] == 10 && num_5 == 0) || (bills[i] == 20 && num_5 == 0)) {
               return false;
           } else if (bills[i] == 5) {
               num_5++;
           } else if (bills[i] == 10 && num_5 >= 1) {
               num_5--;
               num_10++;
           } else if (bills[i] == 20) {
               if (num_10 >= 1 && num_5 >= 1) {
                   num_10--;
                   num_5--;
               } else if (num_5 >= 3) {
                   num_5-=3;
               } else {
                   return false;
               }
           } else {
               return false;
           }
       }
       return true; 
    }
}