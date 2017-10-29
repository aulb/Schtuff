class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Empty string
        if not s: return -1
        
        latin_count = [0] * 26
        for char in s:
            latin_count[ord(char) - 97] += 1
        
        for index, char in enumerate(s):
            ascii_value = ord(char) - 97
            if latin_count[ascii_value] == 1:
                return index
        # Not found
        return -1
