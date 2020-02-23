# No need to do DP if k >= length // 2, buy on every uptick
# Need to make this faster
class Solution:
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices or (k < 1): return 0
        # Keep track of the previous maxes
        previous = [0] * len(prices)
        
        for transaction in range(1, k + 1):
            current = [0] * len(prices)
            for index, price in enumerate(prices):
                current[index] = max(
                    [price - prices[jndex] + previous[jndex] for jndex in range(index)]  + 
                    [0 if index - 1 < 0 else current[index - 1]]
                )
            # No need for current[::], since current is going to be overwritten
            previous = current

        return current[-1]
