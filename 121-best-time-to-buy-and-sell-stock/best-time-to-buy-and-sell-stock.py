class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_buy = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if curr_buy > prices[i]:
                curr_buy = prices[i]
            elif prices[i] - curr_buy > profit:
                profit = prices[i] - curr_buy
        return profit
        

