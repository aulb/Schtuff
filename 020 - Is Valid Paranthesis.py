# Use stack

def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    if len(s) % 2 != 0 or len(s) == 0:
        return False
    lookup = {'(': ')', '[': ']', '{': '}'}
    for _ in range(0, len(s), 2):
        if s[_] in '({[' and s[_ + 1] != lookup[s[_]] or s[_] not in '({[':
            return False
    return True

print isValid('())')
print isValid('([])')
print isValid('[')
print isValid('()()()()()(){}[]{}')
