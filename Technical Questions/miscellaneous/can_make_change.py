def capable_change(n):
	if n < 0: return False 
	if n % 6 == 0 or n % 9 == 0 or n % 20 == 0: return True
	return capable_change(n - 6) or capable_change(n - 9) or capable_change(n - 20)
