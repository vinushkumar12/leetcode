class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        beg = 0
        end = len(s) - 1
        while beg < end:
            if (s[beg] == ' '):
                beg += 1
            elif (s[end] == ' '):
                end -= 1
            elif ((s[beg].isalnum()) == False):
                beg += 1
            elif ((s[end].isalnum()) == False):
                end -= 1
            elif (s[beg] != s[end]):
                return False
            else:
                beg += 1
                end -= 1
        return True
