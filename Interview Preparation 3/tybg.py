# Libraries Included:
# Numpy, Scipy, Scikit, Pandas

"""
Given a string, find the length of the longest substring without repeating characters.

Examples:
Given "abcabcbb", a longest substring without repeats is "abc", the length of which is 3.
Given "bbbbb", the longest substring without repeats is "b", the length of which is 1.
Given "pwwkew", a longest substring without is "wke", the length of which is 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

Given "abacd"
"abcbb"
"""

print("Hello, world!")

def longest_substring_no_repeats(string):
    if not string: return 0

    # front - index all unique characters
    front = 0 # pointer to the front, 
    max_length = 1
    characters = {}
    # find all the unique characters
    for index, character in enumerate(string):
        if character not in characters:
            characters[character] = 0
            max_length = max(max_length, index - front + 1)
        else:
            characters[character] -= 1
            
            # character['a'] : -1, so it goes through 
            if characters[character] == -1:
                max_length = max(max_length, index - front)

            # "abca" front needs to find "a"
            while front < len(string) and string[front] != character:
                characters[string[front]] += 1
                front += 1
            
            # "abcb" -> "bcb"
            if string[front] == character:
                characters[string[front]] += 1
                front += 1
                
        # print(index, front, characters, max_length)
        
    return max_length
                
if __name__ == "__main__":
    string1 = "abcabcbb" # 3
    string2 = "bbbbb" # 1
    string3 = "pwwkew" # 3 
    string4 = "abacd" # 4
    
    print(longest_substring_no_repeats(string1))
    print(longest_substring_no_repeats(string2))        
    print(longest_substring_no_repeats(string3))    
    print(longest_substring_no_repeats(string4))
