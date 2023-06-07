class Solution {
    public int numJewelsInStones(String jewels, String stones) {
        int counter = 0;
        for(int i = 0; i < stones.length(); i++) {
            for(int b = 0; b < jewels.length(); b++ ) {
                if(stones.charAt(i) == jewels.charAt(b)) {
                    counter++;
                    jewels.replace(stones.charAt(i), '*');
                }
            }
        }
        return counter;
    }
}