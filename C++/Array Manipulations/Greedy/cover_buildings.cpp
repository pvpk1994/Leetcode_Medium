// Cover bulidings with canvas 
/* 
Probelm Description:
--------------------
Author: Pavan Kumar Paluri
Problem Description:
There are N rectangular buildings standing along the road next to each other. The K-th building is of size H[K] × 1.
Because a renovation of all of the buildings is planned, we want to cover them with rectangular banners until the renovations are finished. 
Of course, to cover a building, the banner has to be at least as high as the building. We can cover more than one building with a banner if it is wider than 1.
For example, to cover buildings of heights 3, 1, 4 we could use a banner of size 4×3 (i.e. of height 4 and width 3), marked here in blue:
Buildings of sizes (3 × 1), (1 × 1), (4 × 1), covered with scaffolding of size 4×3
We can order at most two banners and we want to cover all of the buildings. Also, we want to minimize the amount of material needed to produce the banners.
What is the minimum total area of at most two banners which cover all of the buildings?
Write a function:
    def solution(H)
that, given an array H consisting of N integers, returns the minimum total area of at most two banners that we will have to order.
Examples:
1. Given H = [3, 1, 4], the function should return 10. 
The result can be achieved by covering the first two buildings with a banner of size 3×2 and the third building with a banner of size 4×1:
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
*/

#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

class Solution{
public:
	int banner_area(vector<int>H)
	{
		// if there are no buildings 
		if(H.size()==0)
			return 0;
		vector<int> left_arr;
		vector<int> right_arr;
		int left_max = 0;
		for(int i=0;i<H.size();i++)
		{
			if(left_max > H[i])
				left_arr.push_back(left_max);
			else
			{
				left_max = H[i];
				left_arr.push_back(left_max);
			}
		}
		// fill out the right array
		int right_max = H[H.size()-1];
		for(int j=H.size()-1; j>=0; j--)
		{
			if(right_max > H[j])
				right_arr.push_back(right_max);
			else{
				right_max = H[j];
				right_arr.push_back(right_max);
			}
		}

		// reverse the right vector:
		reverse(right_arr.begin(), right_arr.end());

		// final loop iteration to compute the costs
		int ans = INT_MAX; 
		for(int i=1; i<H.size(); i++)
		{
			// ans = min(ans, 0);
			int ans1= left_arr[i-1]*i+right_arr[i]*(H.size()-i);
			ans = min(ans, ans1);
		}
		return ans;

	}
};

int main()
{
	Solution sol;
	vector<int>height{3,1,4};
	cout << sol.banner_area(height)<<endl;
	return 0;
}