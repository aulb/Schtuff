def divide(dividend, divisor):
	# Negative integers
	if divisor == 0:
		return MAX_INT

	divisorp = abs(divisor)
	dividendp = abs(dividend)

	r = 0
	while dividendp - divisorp >= 0:
		dividendp = dividendp - divisorp
		r = r + 1



	return r 