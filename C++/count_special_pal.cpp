// Source: HackerRank Medium Question
// Count the number of special substrings in a given string
// Two conditions have to be met:
// conditions: 
// 1. All of the characters are the same, e.g. aaa.
// 2. All characters except the middle one are the same, e.g. aadaa.
#include <iostream>
#include <string>
using namespace std;

int count_substr_palindrome(string& str)
{
	int count = str.size();
	for(int i=0; i<str.size(); i++)
	{
		int diff_char_index = 0;
		for(int j=i+1; j<str.size();j++)
		{
			if(str[i]==str[j])
			{
				if(diff_char_index-i == j- diff_char_index)
				{
					count++;
					break;
				}
				else if(diff_char_index == 0)
					count++;
			}
			else {
				if(diff_char_index==0)
				{
					diff_char_index = j;
				}
				else 
					break;
			}
		}
	}
	return count;
}

int main()
{
	string s ="asasd";
	int result=count_substr_palindrome(s);
	cout << result << endl;
	return 0;
}
