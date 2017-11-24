getTopTen(): returns top ten most frequent events and their exact counts


user_id | timestamp | event_data: JSON

event_data: {
  hierarchy: div.content span button
  action: 'click' | 'submit' 
  ... 
}



Your previous Python 3 content is preserved below:

# pastel 
# {p: 1, a: 1 ...} 

# longest word in the array m

# sorted(pastel) = aelpst
# {aelpst: [pastel, staple]}

# get_anagrams(["pastel", "staple", "banana", "kiwi", "late", "tale"])
#   -> ["pastel", "staple", "late", "tale"]

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
