class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        profit = 0
        b, s = 0, 1

        while s < len(prices):
            if prices[b] >= prices[s]:
                b = s
                s += 1
            elif prices[b] < prices[s]:
                if profit < prices[s] - prices[b]:
                    profit = prices[s] - prices[b]
                s += 1
        return profit 