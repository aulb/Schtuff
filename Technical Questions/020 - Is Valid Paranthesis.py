class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lookup = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        values = list(lookup.values())
        keys = list(lookup.keys())

        lookup_stack = []
        for char in s:
            # Append open brackets, anykind
            if char in values: lookup_stack.append(char)
            # Check for each closing bracket, it matches with the top stack, otherwise no
            elif char in keys:
                # If the length of lookup stack is 0, return false immediately,
                # similarly if the top of the stack is not what we expect
                if len(lookup_stack) == 0 or not (lookup_stack.pop() == lookup[char]): return False
        # The stack should be 0 in the end
        return len(lookup_stack) == 0


# def isValid(s):
#     """
#     :type s: str
#     :rtype: bool
#     """
#     if len(s) % 2 != 0 or len(s) == 0:
#         return False
#     lookup = {'(': ')', '[': ']', '{': '}'}
#     for _ in range(0, len(s), 2):
#         if s[_] in '({[' and s[_ + 1] != lookup[s[_]] or s[_] not in '({[':
#             return False
#     return True

# print isValid('())')
# print isValid('([])')
# print isValid('[')
# print isValid('()()()()()(){}[]{}')
# '{(abc)22}[14(xyz)2]' => True
