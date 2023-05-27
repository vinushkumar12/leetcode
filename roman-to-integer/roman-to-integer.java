class Solution {
    public int romanToInt(String s) {
        int answer = 0;
        for (int i = 0; i < s.length(); i++) {
           if (s.charAt(i) == 'I' && i + 1 < s.length() && s.charAt(i + 1) == 'V') {
               answer += 4;
               i += 1;
           } else if (s.charAt(i) == 'I' && i + 1 < s.length() && s.charAt(i + 1) == 'X') {
               answer += 9;
               i += 1;
           } else if (s.charAt(i) == 'X' && i + 1 < s.length() && s.charAt(i + 1) == 'L') {
               answer += 40;
               i += 1;
           } else if (s.charAt(i) == 'X' && i + 1 < s.length() && s.charAt(i + 1) == 'C') {
               answer += 90;
               i += 1;
           } else if (s.charAt(i) == 'C' && i + 1 < s.length() && s.charAt(i + 1) == 'D') {
               answer += 400;
               i += 1;
           } else if (s.charAt(i) == 'C' && i + 1 < s.length() && s.charAt(i + 1) == 'M') {
               answer += 900;
               i += 1;
           } else if (s.charAt(i) == 'I') {
               answer += 1;
           } else if (s.charAt(i) == 'V') {
               answer += 5;
           } else if (s.charAt(i) == 'X') {
               answer += 10;
           } else if (s.charAt(i) == 'L') {
               answer += 50;
           } else if (s.charAt(i) == 'C') {
               answer += 100;
           } else if (s.charAt(i) == 'D') {
               answer += 500;
           } else if (s.charAt(i) == 'M') {
               answer += 1000;
           }
        }
        return answer;
    }
}   