// Find the Kth-smallest element in an unsorted array in C++
// Author: Pavan Kumar Paluri

// Kth smallest element

#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int kth_smallest(vector<int>&v, int k){
	priority_queue<int> pq;
	for(int i=0; i<k; i++)
	{
		pq.push(v[i]);
	}
	// cout << "check1" << endl;
	// if here, we have k elements in the pq now
	for(int i=k; i<v.size(); i++)
	{
		// cout << "check1.2" << endl;
		if(v[i] < pq.top())
		{
			// pop the top most element from the pq
			// cout << "check2" << endl;
			pq.pop();
			pq.push(v[i]);
		}
	}

	// if here the last element in the pq should be the desired element
	int temp = pq.top();
	while(!pq.empty())
	{
		int temp = pq.top();
		pq.pop();
	}
	// cout << "temp is: " << temp << endl;
	return temp;
}
int main()
{
	vector<int>v {-1,3,1,4,2,21,41,3,11};
	int result = kth_smallest(v, 4);
	cout << result << endl;
	return 0;
}
