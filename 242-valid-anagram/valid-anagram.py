class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = dict()
        for i in s:
            if i in a:
                a[i] += 1
            else:
                a[i] = 1
        for i in t:
            if i in a:
                a[i] -= 1
                if a[i] == 0:
                    del a[i]
            else:
                return False
        if a:
            return False
        return True