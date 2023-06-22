class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = sys.maxsize
        profit = -sys.maxsize
        for i in prices:
            if (i < low):
                low = i
            elif (profit < i - low):
                print(i)
                print(low)
                profit = i - low
        if (profit == -sys.maxsize):
            return 0
        return profit

