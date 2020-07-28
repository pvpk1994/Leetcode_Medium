// Author: Pavan Kumar Paluri
// Find first and last indices of the target element in a sorted array 
// Time complexity should not exceed O(logN) where N is the number of elements
// Option 1: To use 2-pass linear search to find the start and end indices of the list
// Option 2: To use 3-pass binary search to find the indices of first and last occurrence of the intended target element

class Solution {
public:
    int search_left(vector<int>&arr, int low, int high, int target)
    {
        while(low < high)
        {
            int mid =  low+int((high-low)/2);
            if(arr[mid] < target)
            {
                low = mid+1;
            }
            // mid-1 cannot go into negative values 
            else if( mid-1 > 0 && arr[mid-1] < target)
            {
                return mid;
            }
        else{
                high = mid-1;
            }
        }
        // If none found: return low 
        return low;
    }
    
    int search_right(vector<int>&arr, int low, int high, int target)
    {
        while(low < high)
        {
            int mid = low + int((high-low)/2);
            if(arr[mid] > target)
            {
                high = mid-1;
            }
            else if(arr[mid+1]>target)
                return mid;
            else{
                low = mid+1;
            }
        }
        // If none found: return high
        return high;
    }
    vector<int> searchRange(vector<int>& nums, int target) {
        int low = 0;
        int high = nums.size()-1;
        vector<int>output;
        while(low <= high)
        {
            int mid = low + int((high-low)/2);
            if(nums[mid] < target){
                // target larger, move towards the right
                low = mid+1;
            }
            else if(nums[mid]>target)
            {
                high = mid-1;
            }
            else{
                output.push_back(search_left(nums, 0, mid, target));
                //output.push_back(0);
                output.push_back(search_right(nums, mid, nums.size()-1, target));
                return output;
            }
        }
        output.push_back(-1);
        output.push_back(-1);
        return output;
    }
};
