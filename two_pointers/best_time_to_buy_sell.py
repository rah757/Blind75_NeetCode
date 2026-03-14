class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 101
        max_profit = 0
        day = 0

        while day != len(prices):
            if prices[day] < min_price:
                min_price = prices[day]
            if prices[day] - min_price > max_profit:
                max_profit = prices[day] - min_price
            day += 1

        return max_profit
