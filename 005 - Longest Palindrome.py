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


# def longestPalindrome(self, s):
#     res = ""
#     for i in xrange(len(s)):
#         # odd case, like "aba"
#         tmp = self.helper(s, i, i)
#         if len(tmp) > len(res):
#             res = tmp
#         # even case, like "abba"
#         tmp = self.helper(s, i, i+1)
#         if len(tmp) > len(res):
#             res = tmp
#     return res
 
# # get the longest palindrome, l, r are the middle indexes   
# # from inner to outer
# def helper(self, s, l, r):
#     while l >= 0 and r < len(s) and s[l] == s[r]:
#         l -= 1; r += 1
#     return s[l+1:r]
# Just normal O(n^2) solution iterate from point till end.

if __name__ == '__main__':
	print longestPalindrome("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") # 8 => 64
