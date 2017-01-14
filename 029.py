def divide(dividend, divisor):
	# Negative integers
	if divisor == 0:
		return 0

	divisorp = abs(divisor)
	dividendp = abs(dividend)

	# Cases for negative and positive
	neg = (dividend < 0 and divisor > 0) or (divisor < 0 and dividend > 0)
	r = 0
	while dividendp - divisorp >= 0:
		dividendp = dividendp - divisorp
		r = r + 1
	return r if not neg else -r

	# Multiply multiply multiply by 2
	# If woopsie, go back one


# Nice trick from discussion for bit division
    # c,sub=1,divisor;

    # while(dividend >= divisor):
    #     if(dividend>=sub):
    #         dividend-=sub;
    #         ret+=c;
    #         sub=(sub<<1);
    #         c=(c<<1);
    #     else:
    #         sub=(sub>>1);
    #         c=(c>>1);
