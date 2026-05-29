class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum_before = 101 # max 100
        profit = []

        for i in range(len(prices)):
            profit.append(prices[i] - minimum_before)

            minimum_before = min(minimum_before, prices[i])

        soln = max(profit)
        if soln < 0:
            return 0;

        return soln