class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # Question: can needle be arbitrarily long?
        # Needle is arbitrarily long
        # What to do for empty string as needle return 0? len haystack < needle: return -1
        if not needle: return 0
        if len(haystack) < len(needle): return -1
        
        for index in range(len(haystack)):
            # Find first instance of letter, check if the substring is the same
            if haystack[index] == needle[0]:
                end = len(needle) + index
                if end <= len(haystack) and haystack[index:end] == needle: return index
            
        return -1
