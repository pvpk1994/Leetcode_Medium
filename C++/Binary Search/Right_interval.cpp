// Leetcode - medium
// Sort + Binary Search - O(NlogN) 
// Author: Pavan Kumar Paluri

class Solution {
public:
    int bs(vector<vector<int>>& in, int v) {
        int l=0,n=in.size(),h=n-1;
        
        while(l<=h) {
            int m = l + (h-l)/2;
            
            if(in[m][0] < v) {
                l=m+1;
            }
            else {
                h=m-1;
            }
        }
        
        return l<n ? l : -1;
    }
    
    
    vector<int> findRightInterval(vector<vector<int>>& in) {
        
        int n = in.size();
        vector<int> ans (n, -1); 
        
	// Store the index of each interval along side
	// the start and end points.
	// Will help post-sorting.
        for(int i=0; i<n; ++i) {
            in[i].push_back(i);
        }
        
	// Sort in non-decreasing order with respect to the start points.
	// If start points are equal,  use end points.
        sort(in.begin(), in.end(), [](const vector<int>& a, const vector<int>& b) {
            if(a[0] == b[0])
                return a[1]<b[1];
            return a[0]<b[0];
        });
        
        for(int i=0; i<n; ++i) {
            int ix = in[i][2];
            int px = bs(in, in[i][1]);
            if(px != -1)
                ans[ix] = in[px][2];
        }
        
        return ans;
    }
};
