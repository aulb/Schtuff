'''
Given a set of strings, e.g. {“one”,"on", “two”, “four”}, and a target string, e.g. “fouroneone”, return true if the target string is composed of elements from the set.

“fouroneone” -> true # "four" -> recurse("oneone")
“fouron” -> false
“twone” -> false

"fourtwo" -> true
"one" -> true
'''
def composed_of(s, wordDict):  
    """
    wordDict = ["on", "one", "two", "four"]
    s1 = "fouroneone"
    """
    # Transform the wordDict to hash table
    string_hash = {}
    for key in wordDict:
        string_hash[key] = True 
    
    def is_composed_of(s): # 'on'
        # Base case, wordDict does not contain any empty string
        # s is also not ""
        if s == "": return True

        # iterate through the s, i from 1 to len(s)
        for i in range(1, len(s) + 1):
            # to check the whole array
            
            if string_hash.get(s[0:i], False): 
                return is_composed_of(s[i:]) 

        return False
    
    return is_composed_of(s)
    

### TEST CASES ###

s2 = "fouron"
s3 = "twone"

assert composed_of(wordDict, s1) == True
assert composed_of(wordDict, s2) == True
assert composed_of(wordDict, s3) == False

# 1 to n, we don't have to worry about empty string ""
# for every s[0:i] if its in the array then slice
# recurse until s is empty


# Brute force solution
# Iterate through the wordDict, and check if 
# "one" checking against ["two", "one", "four"] 


# def say_hello():
#     print('Hello, World')

# for i in range(5):
#     say_hello()
