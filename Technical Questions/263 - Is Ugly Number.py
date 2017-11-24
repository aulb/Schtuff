def isUgly(num):
    # Negative numbers might have -2, -3, -5 as primes, immediately no
    if num <= 0: return False
	# isinstance is a function    
    # Biggest number
    for i in [2, 3, 5]:
        while num % i == 0:
            num = num / i    
    return num == 1
