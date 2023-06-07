class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        my_set, my_set2 = {},{}
        for i in range(len(s)):
            my_set[s[i]] = 1 + my_set.get(s[i], 0)
            my_set2[t[i]] = 1 + my_set2.get(t[i], 0)
        return my_set2 == my_set