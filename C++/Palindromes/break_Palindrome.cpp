// Break Palindrome
// Author: Pavan Kumar Paluri
// Time Complexity: O(N) and Space Complexity: O(1)
#include <iostream>
#include <string>
using namespace std;

class Solution{
public:
	string break_palindrome(string pal)
	{
		int len_pal = pal.size();
		for(int i=0; i<len_pal/2; i++)
		{
			// if a non-a: replace it
			if(pal[i]!='a')
			{
				pal[i]='a';
				return pal;
			}
			else
				continue;
		}

		// if all a's encountered, replace the last a with a b to obtain lexicographically smallest string
		if(pal.size()>1)
			pal[len_pal-1]='b';
		else 
			pal="";
		return pal;
	}
};

int main()
{
	Solution sol;
	cout << sol.break_palindrome("malayalam") << endl;
	return 0;
}
