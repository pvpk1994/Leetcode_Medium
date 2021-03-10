// Balanced Brackets using concept of Stack
// Author: Pavan Kumar Paluri
// Time and Space Complexity; O(N) and O(N)
// Algo Expert Question: https://www.algoexpert.io/questions/Balanced%20Brackets

using namespace std;

// O(N) time and O(N) space 
bool balancedBrackets(string str) {
  // Write your code here.
	unordered_map<char, char>h_map{ {']','['},
																				{')','('},
																				{'}','{'} };
	unordered_set<char>hash_set = {'[',']','{','}','(',')'};
	vector<char>stack (1, '*'); // init stack with a single '*' char
	for(int i=0; i<str.size(); i++)
	{
		// if element not present in hash_set 
		if((hash_set.find(str[i])!=hash_set.end()) && (h_map.find(str[i])==h_map.end()))
			 {
				 stack.push_back(str[i]);
			 }
		else if((hash_set.find(str[i])!=hash_set.end()) && (h_map.find(str[i])!=h_map.end()))
			 {
				 if(stack.back() == h_map[str[i]])
				 {
					 stack.pop_back();
				 }
				 else
					 return false;
			 }
	}
  return stack.back() == '*';
}
