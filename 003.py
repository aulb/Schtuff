"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Corner case, length is 1
        if len(s) == 1:
        	return 1

        # Gets empty string
        top_length = 0
        helper = []
        for ss in s:
        	# If letter is found, record length
        	# "Pop" until that index
        	if ss in helper:
        		if top_length < len(helper):
        			top_length = len(helper)

        		# find the offender and cut from there onwards
        		helper = helper[helper.index(ss) + 1:]
        		print helper
        	helper.append(ss)

    	# At the very end, check again
        if top_length < len(helper):
        	top_length = len(helper)
       	return top_length



