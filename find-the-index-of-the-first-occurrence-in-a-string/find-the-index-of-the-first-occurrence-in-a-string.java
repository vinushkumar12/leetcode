class Solution {
    public int strStr(String haystack, String needle) {
        if (haystack.equals(needle)) {
            return 0;
        }
        for (int i = 0; i < haystack.length(); i++) {
            if (needle.length() == 1 && i + 1 == haystack.length() && needle.charAt(0) == haystack.charAt(i)) {
                return i;
            }
            if (i + needle.length() - 1 < haystack.length() && needle.equals(haystack.substring(i, i + needle.length()))) {
                return i;
            }
        }
        return -1;
        
    }
}