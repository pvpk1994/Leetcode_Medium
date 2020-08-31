// Finding the Maximum Difference between 2 elements in an array A[i]-A[j] such that i >= j
// Author: Pavan Kumar Paluri


#include <iostream>
#include <vector>
#include <climits>
// Max diff between two numbers such that j>=i in A[j]-A[i]
// O(N) approach
using namespace std;

int main()
{
    vector<int>v {1, 2, 90, 10, 110};
    // vector<int> min_v;
    // linear pass approach
    int min_v=v[0];
    int max_result = INT_MIN;
    for(int i=0; i<v.size(); i++)
    {
        if(min_v > v[i])
        min_v = v[i];
        if((v[i]-min_v) > max_result)
        max_result = v[i]-min_v;
    }
    cout << "Max result: " << max_result << endl;
}
