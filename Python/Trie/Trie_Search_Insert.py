# Trie Search and Insert Operations 
# Author: Pavan Kumar Paluri
# Time Complexity: O(N*L)

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # INIT A hashmap
        self.tracker = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        current = self.tracker
        for character in word:
            # iterate through each character of the word 
            if character not in current:
                current[character] = {}
            current = current[character]
        # If here: terminated after iterating through the word
        current['*'] = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        current = self.tracker
        # go character by character 
        for character in word:
            if character not in current:
                return False
            # else : if it is, proceed deeper
            current = current[character]
        # if here:
        # if current has '*': return True, else False
        if '*' in current:
            return True
        else:
            return False
    

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        current = self.tracker
        for char in prefix:
            if char not in current:
                return False
            current = current[char]
        # if here: prefix iteration is over:
        # Now: need to make sure character 
        if current is not None:
            return True
        else:
            return False
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
