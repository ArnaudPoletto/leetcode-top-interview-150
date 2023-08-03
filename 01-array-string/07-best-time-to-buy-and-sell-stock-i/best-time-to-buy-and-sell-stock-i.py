class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # SOLUTION 1: faster using buy and sell pointers
        buy = 0
        sell = 1
        max_profit = 0
        while sell < len(prices):
            curr_profit = prices[sell] - prices[buy]
            if prices[buy] < prices[sell]:
                max_profit = max(curr_profit, max_profit)
            else:
                buy = sell
            sell += 1
        
        return max_profit

        # SOLUTION 2: slow method using min/max arrays
        '''
        # Get minimum potential buy price from time i
        min_prices = prices[0:1]
        for i in range(1, len(prices)):
            min_prices.append(min(prices[i], min_prices[i-1]))

        # Get maximum potential buy price from time i
        max_prices = prices[len(prices)-1:len(prices)]
        for i in range(len(prices)-2, -1, -1):
            max_prices.append(max(prices[i], max_prices[len(prices)-2-i]))
        max_prices = max_prices[::-1]
        max_prices = max_prices[1::]

        diff = [max_price - min_price for (min_price, max_price) in zip(min_prices, max_prices)]

        print(min_prices, max_prices, diff)

        if len(diff) == 0:
            return 0

        best_buy = max(max(diff), 0)
        return best_buy
        '''

