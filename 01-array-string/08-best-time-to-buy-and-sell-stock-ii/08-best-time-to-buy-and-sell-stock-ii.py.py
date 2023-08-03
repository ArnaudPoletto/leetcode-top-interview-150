from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # SOLUTION 1: using range
        return sum(max(prices[i+1] - prices[i], 0) for i in range(0, len(prices)-1))

        # SOLTUION 2: using pairwise
        return sum(max(sell - buy, 0) for buy, sell in pairwise(prices))