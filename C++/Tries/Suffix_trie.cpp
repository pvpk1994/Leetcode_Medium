// Suffix Trie Construction
// Author: Pavan Kumar Paluri
// AlgoExpert Question: https://www.algoexpert.io/questions/Suffix%20Trie%20Construction
// Time Complexity: O(N*2) Space: O(N*2) for populateSuffixTrieFrom()
// Time Complexity: O(M) Space: O(1)

#include <unordered_map>
using namespace std;

// Do not edit the class below except for the
// populateSuffixTrieFrom and contains methods.
// Feel free to add new properties and methods
// to the class.
class TrieNode {
public:
  unordered_map<char, TrieNode *> children;
};

class SuffixTrie {
public:
  TrieNode *root;
  char endSymbol;

  SuffixTrie(string str) {
    this->root = new TrieNode();
    this->endSymbol = '*';
    this->populateSuffixTrieFrom(str);
  }

  void populateSuffixTrieFrom(string str) {
    // Write your code here.
		for(int i=0; i<str.size(); i++)
		{
			// init the node 
			TrieNode *node = root;
			for(int j=i; j<str.size(); j++)
			{
				if(node->children.find(str[j])==node->children.end()) // not found
				{
					// element str[j] not found -> create a new unordered map for that
					TrieNode *new_node = new TrieNode();
					// set node to this
					node->children.insert({str[j], new_node});
				}
				// if already present, change the key to that
				node = node->children[str[j]];
			}
			// now insert '*' at the end of each sub-list
			node->children.insert({this->endSymbol, nullptr});	
		}
  }

  bool contains(string str) {
    // Write your code here.
		TrieNode *node = this->root;
		for(int i=0; i< str.size(); i++)
		{
			if(node->children.find(str[i])==node->children.end()) // if not found
				return false;
			// if found
			node = node->children[str[i]];	
		}
		// if suffix is to be found: make sure the last key is '*'
		if(node->children.find(this->endSymbol) != node->children.end()) // if found
			return true;
    else
			return false;
  }
};

