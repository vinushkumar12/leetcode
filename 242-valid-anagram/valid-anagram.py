class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        holder = {}
        for i in s:
            if i in holder: 
                holder[i] += 1
            else:
                holder[i] = 1
        for i in t:
            if i in holder:
                holder[i] -= 1
                if holder[i] == 0:
                    del holder[i]
            else:
                return False
        if (holder):
            return False
        return True