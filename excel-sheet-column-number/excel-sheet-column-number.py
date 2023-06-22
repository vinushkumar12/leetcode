class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        pos = 0
        ans = 0
        for i in range(len(columnTitle) - 1, -1, -1):
            ans = ans + ((ord(columnTitle[i]) - 64) * (26 ** pos))
            pos = pos + 1
        return ans
