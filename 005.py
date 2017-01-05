"""
https://leetcode.com/problems/longest-palindromic-substring/
"""
# Base, palindromic, length 1 is palindrome
# AABBA
# ---?---?---

# Two pointers
# A[0] A[-1]
# ???
class Solution(object):
    def __init__(self):
        self.cache = {}
    
    def aux(self, s):
    	# If in cache return
    	if s in self.cache:
    		return self.cache[s]
    
    	# Otherwise calculate
    	if len(s) - 2 < 0:
    		self.cache[s] = True
    		return True
    	elif s[0] == s[len(s) - 1]:
    		self.cache[s] = self.aux(s[1:len(s) - 1])
    		return self.cache[s]
    	else:
    		self.cache[s] = False
    		return False
    
    def longestPalindrome(self, s):
    	"""
    	:type s: str
    	:rtype: str
    	"""
    	# Corner cases
    	strlen = len(s)
    	longest = ''
    
    	for i in range(0, strlen):
    		for j in range(strlen - 1, -1, -1):
    			# if s@i,j is the same then check w aux
    			if s[i] == s[j]:
    				# if they're palindromic, break
    				check = s[i:j+1]
    				if self.aux(check) and len(longest) < len(check):
    					longest = check
    					# onto the next substring
    					break
		# refresh cache
        self.cache = {}
    	return longest

if __name__ == '__main__':
	print longestPalindrome("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") # 8 => 64
