// kth factor of n
// using min heap data structure
// Author: Pavan Kumar Paluri
// Time Complexity: O(sqrt(N))
// Space Complexity: O(min(sqrt(N), k))

class Solution {
public:
    int kthFactor(int n, int k) {
        priority_queue<int> min_pq;
        for(int i=1; i<int(sqrt(n))+1; i++)
        {
            if(n%i ==0)
            {
                // push the element into the max-heap
                if(min_pq.size() < k)
                    min_pq.push(i);
                else{
                    if(min_pq.top()> i)
                    {
                        min_pq.pop();
                        min_pq.push(i);
                    }
                }
                if(i!= n/i)
                {
                    // push the element into the max-heap
                if(min_pq.size() < k)
                    min_pq.push(n/i);
                else{
                    if(min_pq.top()> i)
                    {
                        min_pq.pop();
                        min_pq.push(n/i);
                    }
                }
                }
            }
        }
 
        // the top-most element is always a given kth element in ascending order
        if(k<= min_pq.size())
            return min_pq.top();
        else
            return -1;
    }
};
