import re

# Don't forget * is 0, inf match
# Capture anything, repeat of that captured item 0 to as many times
match = re.compile(r'((.)\2*)')

# >>> match.findall('112222')
# [('11', '1'), ('2222', '2')]
# "group", "duplicate"
# https://stackoverflow.com/questions/1739514/underscore-as-variable-name-in-python
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        string = '1' # The first one
        for i in range(n - 1):
            # Lots of groups
            string = "".join([str(len(group)) + digit for group, digit in match.findall(string)])

        return string
