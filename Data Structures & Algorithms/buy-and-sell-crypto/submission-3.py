class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        l = len(prices)
        if l == 1:
            return 0
        i, j = 0, 1
        min_so_far = float("+inf")
        while j < l:
            min_so_far = min(min_so_far, prices[i])
            profit = prices[j] - prices[i]
            best = max(profit, best)
            if (prices[i] > prices[j]):
                i = j
            j += 1
        return best
