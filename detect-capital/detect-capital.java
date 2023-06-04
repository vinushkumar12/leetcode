class Solution {
    public boolean detectCapitalUse(String word) {
        if(word.equals(word.toLowerCase()) || word.equals(word.toUpperCase()) || word.equals(word.substring(0,1).toUpperCase() + word.substring(1, word.length()).toLowerCase())) {
            return true;
        }
        return false;
    }
}