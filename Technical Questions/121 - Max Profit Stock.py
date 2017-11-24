def max_profit(prices):
	if len(prices) == 0: return 0

	max_price = prices[0]
	min_price = prices[0]
	max_difference = 0

	# Min price needs to come after
	for price in prices:
		if max_price < price:
			max_price = price
			if (max_difference < max_price - min_price):
				max_difference = max_price - min_price
		elif min_price > price:
			min_price = price
			max_price = price
			
	return max_difference

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        min_so_far = max_so_far = prices[0]
        max_profit = 0
        
        for price in prices:
            # Reset everything if new minimum found
            if price < min_so_far: min_so_far = max_so_far = price
            
            max_so_far = max(max_so_far, price)
            max_profit = max(max_profit, max_so_far - min_so_far)
            
        return max_profit
