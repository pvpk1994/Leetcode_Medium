# Count the number of sentences using conept of Anagrams
# Author: Pavan Kumar Paluri
# Rivian Automotive Interview Question 
# Modified into O(N^2)
from collections import Counter
from collections import defaultdict  

def count_sentences(word_set:list, sentence_set:list)->list:
	lsit_output = []
	dict_words = defaultdict(list)
	for word in word_set:
		dict_words[tuple(sorted(word))].append(word)
	# Now make a list of all the values of key-value pairs
	list_words = list(dict_words.values())

	# Now iterate through the list of sentences 
	for sentence in sentence_set:
		list_s = sentence.split(" ")
		counter = 0
		for s in list_s:
			if tuple(sorted(s)) in dict_words.keys() and len(dict_words[tuple(sorted(s))]) > 1:
				counter += len(dict_words[tuple(sorted(s))])
		lsit_output.append(counter)
	return lsit_output

if __name__ == '__main__':
	print(count_sentences(["silent", "listen", "in"], ["listen is silent"]))
	# print(count_sentences(["the", "bats", "tabs", "cat", "act", "in"], ["cat the bats", "in the act", "act tabs in"]))





