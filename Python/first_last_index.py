# Find first and last indices of the target element in a sorted array 
# Time complexity should not exceed O(logN) where N is the number of elements
# Option 1: To use 2-pass linear search to find the start and end indices of the list
# Option 2: To use 3-pass binary search to find the indices of first and last occurrence of the intended target element

# Author: Pavan Kumar Paluri
def searchRange(nums: list, target: int)->list:
  low = 0
  high = len(nums)-1
  while low <= high:
    mid = low + (high-low)//2
    if nums[mid] > target:
      # target is lower, search towards left
      high = mid-1
    elif nums[mid] < target:
      # target is higher, search towards right
      low = mid+1
    else:
      return [search_left(nums, 0, mid, target), search_right(nums, mid, len(nums)-1, target)]
  return [-1, -1] # If target not found at all...

def search_left(nums, low, high, target):
  while low < high:
    mid = low + (high-low)//2
    # Always make a left-probe here.. no need to explore right side
    # i.e., nums[mid] > target 
    if nums[mid] < target:
      low = mid+1
    elif nums[mid-1] < target:
      return mid # We exactly are at the index just before the intended target element's first occurrence 
    else:
      high = mid-1
  # if none found: return low
  return low

def search_right(nums, low, high, target):
  while low < high:
    mid = low + (high-low)//2
    # Make a right-probe here, no need to explore the left subtree 
    if nums[mid] > target:
      high = mid-1
    elif nums[mid+1] > target:
      return mid
    else:
      low = mid+1
  return high

if __name__=="__main__":
  print(searchRange([1,1,2], 1))



