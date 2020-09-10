# Bulls and Cows problem
# Leetcode Question: https://leetcode.com/problems/bulls-and-cows/
# Author: Pavan Kumar Paluri
# Double Linear Pass: One for Bull count and another for Cow Count

from collections import Counter
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        num_bulls = 0
        num_cows =0
        
        
        for i,character in enumerate(secret):
            #print(guess)
            if guess[i] == character:
                # If character is in guess and its index matches
                num_bulls += 1
                # make that character a dummy one now 
                guess = guess[:i]+"X"+guess[i+1:]
                secret = secret[:i]+"Y"+secret[i+1:]
                
        s_counter = Counter(secret)
        g_counter = Counter(guess) 
        hash_set = set()
        
        for i,character in enumerate(secret):
            if character in g_counter and character not in hash_set:
                num_cows += min(s_counter[character], g_counter[character])
                hash_set.add(character)
                # secret = secret[:i]+"Y"+secret[i+1:]
        return str(num_bulls)+"A"+str(num_cows)+"B"
