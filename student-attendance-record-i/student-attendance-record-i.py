class Solution:
    def checkRecord(self, s: str) -> bool:
        if (s.count('A') >= 2):
            print("he")
            return False
        elif (s.find("LLL") != -1):
            return False
        return True