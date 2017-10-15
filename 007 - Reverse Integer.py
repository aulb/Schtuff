def reverse(x):
	"""
	:type x: int
	:rtype: int
	"""
	t = False
	if x < 0: 
	    t = True
	    x = x * -1
	
	result = 0
	while x is not 0:
		result = result * 10 + x % 10    	
		x = x / 10			
	
	if t:
	    result = result * -1
	return result    
        
    # Overflow case
