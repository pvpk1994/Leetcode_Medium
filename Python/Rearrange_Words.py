# Rearrange words based on their lengths.
# In case of a tiebreaker, just preserve the original order of words
# Author: Pavan Kumar Paluri
# Time Complexity: O(NlogN) 

class Solution:
    def arrangeWords(self, text: str) -> str:
        char_c = text[0].lower()
        text = text.replace(text[0], char_c)
        list_text = text.split(" ")
        '''
        h_map=defaultdict(list)
        list_str = []
        for ind,word in enumerate(list_text):
            h_map[len(word)].append(word)
        '''
        # O(NlogN) time complexity
        list_text = sorted(list_text, key=lambda x:len(x))
        list_text[0]=list_text[0].capitalize()
        # print(list_text)
        s=""
        s= s+''.join(i+' ' for i in list_text)
        return s[0:len(s)-1]
