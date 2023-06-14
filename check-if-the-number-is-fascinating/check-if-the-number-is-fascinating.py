class Solution:
    def isFascinating(self, n: int) -> bool:
        nums = str(n) + str(n * 2) + str(n * 3)
        ans = set()
        for i in nums:
            if (i in ans or i == "0"):
                return False
            ans.add(i)
        temp = 267534801
        return True