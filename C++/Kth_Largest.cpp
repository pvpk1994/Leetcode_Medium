// Find the Kth Largest element in an unsorted array
// Auhtor: Pavan Kumar Paluri
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        // Lowest to highest priority queue
        priority_queue<int, std::vector<int>, std::greater<int>>my_pq;
        for(int i=0; i<k && k<=nums.size(); i++)
        {
            // smallest upto kth largest from nums
            my_pq.push(nums[i]);
        }
        for(int i=k; i<nums.size();i++)
        {
            // look if the element 
            if(my_pq.top() < nums[i])
            {
                // if so: exclude 
                my_pq.pop();
                my_pq.push(nums[i]);      
            }
        }       
        return my_pq.top();  
    }
};
