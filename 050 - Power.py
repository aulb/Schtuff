class Solution(object):
    def aux(self, x, n):
        if n == 0:
            return 1
        elif n == 1:
            return x
        i = 1
        base = x
    
        # log(n) solution?
        while i <= abs(n) / 2: 
    		x = x * x
    		i = i * 2
    
    	q = abs(n) - i
    	return x * self.aux(base, q)
    
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
        	return 1
    
        return self.aux(x, n) if n > 0 else 1 / float(self.aux(x, n))