from collections import Counter
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = []
        visited = [False] * len(strs)
        
        for i, word in enumerate(strs):
            if visited[i]: continue
            # eat
            current_result = []
            current_word_counter = Counter(word)
            
            for j, word_to_compare in enumerate(strs):
                if visited[j]: continue
                # Compare counters
                compare_word_counter = Counter(word_to_compare)
                if current_word_counter == compare_word_counter:
                    current_result.append(word_to_compare)
                    visited[j] = True
            result.append(current_result)
            visited[i] = True
        return result

def get_anagrams(words):
    lookup = {}
    result = []
    
    for word in words:
        key = ''.join(sorted(word))
        # Check if the key exist
        if lookup.get(key, False):
            lookup[key].append(word)
        # Key does not exist in the lookup
        else:
            lookup[key] = [word]
    
    for anagrams in lookup.values():
        # If the anagrams length is 1, it doesn't have any other pairs
        if len(anagrams) != 1: 
            result.extend(anagrams)
    
    return result
    
if __name__ == "__main__":
    a = get_anagrams(["pastel", "staple", "banana", "kiwi", "late", "tale"])
    print(a)
