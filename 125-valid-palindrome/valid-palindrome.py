class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = ""
        for i in s:
            if i.isalnum():
                a = a + i.lower()
        for i in range(len(a)):
            if i > len(a) - 1 - i:
                return True
            if a[i] != a[(len(a) - 1) - i]:
                return False
        return True
        