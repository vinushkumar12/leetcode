class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sets = set()
        left = 0
        maximum = 0
        for i in range(len(s)):
            print(maximum)
            while s[i] in sets:
                sets.remove(s[left])
                left += 1
            sets.add(s[i])
            maximum = max(maximum, i - left + 1)
        return maximum


            
        