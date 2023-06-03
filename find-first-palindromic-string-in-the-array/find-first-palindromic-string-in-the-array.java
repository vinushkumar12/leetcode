class Solution {
    public String firstPalindrome(String[] words) {
      for (int i = 0; i < words.length; i++) {
          int end = words[i].length() - 1;
          for (int x = 0; x < words[i].length(); x++) {
              if (words[i].charAt(x) != words[i].charAt(end)) {
                 break;
              } else if (end == x && words[i].charAt(x) == words[i].charAt(end)) {
                  return words[i];
              }
              if (x + 1 == end) {
                  return words[i];
              }
              end--;
          }
      }
      return "";  
    }
}