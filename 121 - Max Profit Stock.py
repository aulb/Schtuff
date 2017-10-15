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