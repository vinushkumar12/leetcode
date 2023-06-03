class Solution {
    public int mostWordsFound(String[] sentences) {
        int max_sentence = 0;
        if (sentences == null) {
            return 0;
        }
        for (int i = 0; i < sentences.length; i++) {
            int temp = sentences[i].length() - sentences[i].replace(" ", "").length();
            if (temp + 1 > max_sentence) {
                max_sentence = temp + 1;
            }
        }
        return max_sentence;
        
    }
}