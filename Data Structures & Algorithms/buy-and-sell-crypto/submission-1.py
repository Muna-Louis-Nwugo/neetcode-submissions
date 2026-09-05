class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        p1 = 0
        p2 = 1
        max_profit = 0

        while p2 < len(prices):
            profit = prices[p2] - prices[p1]

            if profit > max_profit:
                max_profit = profit

            if profit < 0:
                p1 += 1
                p2 += 1
            else:
                p2 += 1
        
        while p1 < len(prices):
            profit = prices[-1] - prices[p1]

            if profit > max_profit:
                max_profit = profit
            
            p1 += 1

        return max_profit