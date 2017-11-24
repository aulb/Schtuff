# https://leetcode.com/problems/implement-trie-prefix-tree/description/
class TrieNode():
    def __init__(self):
        """
        Initialized my helper node here.
        """
        self.children = {}
        self.end_of_word = False
        

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

        
    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        if not word: return
        
        previous = self.root.children.get(word[0], TrieNode())
        previous.end_of_word = 1 == len(word)
        self.root.children[word[0]] = previous
        for i in range(1, len(word)):
            current = previous.children.get(word[i], TrieNode())
            # Don't overwrite end_of_word when inserting
            current.end_of_word = i == len(word) - 1 or current.end_of_word
            previous.children[word[i]] = current
            previous = current
        
        
    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        if not word: return False
        
        previous = self.root.children.get(word[0], None)
        for i in range(1, len(word)):
            if not previous: return False
            previous = previous.children.get(word[i], None)
        
        return previous is not None and previous.end_of_word
    
    
    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        if not prefix: return False
        
        previous = self.root.children.get(prefix[0], None)
        for i in range(1, len(prefix)):
            if not previous: return False
            previous = previous.children.get(prefix[i], None)
            
        return not not previous
        
        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
