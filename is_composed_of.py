'''
Given a set of strings, e.g. {“one”,"on", “two”, “four”}, and a target string, e.g. “fouroneone”, return true if the target string is composed of elements from the set.

“fouroneone” -> true # "four" -> recurse("oneone")
“fouron” -> false
“twone” -> false

"fourtwo" -> true
"one" -> true
'''
def composed_of(string_array, target_string): # Rename this
    # Transform the string_array to hash table
    string_hash = {}
    for key in string_array:
        string_hash[key] = True
    
    def is_composed_of(target_string):
        # Base case, string_array does not contain any empty string
        # target_string is also not ""
        if target_string == "": return True

        can_split = False
        # iterate through the target_string, i from 1 to len(target_string)
        for i in range(1, len(target_string) + 1):
            # to check the whole array
            
            if string_hash.get(target_string[0:i], False):
                can_split = is_composed_of(target_string[i:])
                if can_split:
                    return True

        return can_split
    
    return is_composed_of(target_string)
    

### TEST CASES ###
string_array = ["on", "one", "two", "four"]
target_string1 = "fouroneone"
target_string2 = "fouron"
target_string3 = "twone"

assert composed_of(string_array, target_string1) == True
assert composed_of(string_array, target_string2) == True
assert composed_of(string_array, target_string3) == False

# 1 to n, we don't have to worry about empty string ""
# for every target_string[0:i] if its in the array then slice
# recurse until target_string is empty


# Brute force solution
# Iterate through the string_array, and check if 
# "one" checking against ["two", "one", "four"] 


# def say_hello():
#     print('Hello, World')

# for i in range(5):
#     say_hello()
