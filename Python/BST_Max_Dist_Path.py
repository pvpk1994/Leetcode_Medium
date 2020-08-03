# Finding Maximum Distant Path in a Binary Search Tree
# Coding Interview Question
# Author: Pavan Kumar Paluri

import math
class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def find_max_distant_path(current:Node)->int:
  #current = T
  list_len= []
  max_num = -math.inf
  def helper(current, str_gv, list_len, max_num):
    ''''
    if current is not None and current.val not in node_list_uniq:
      node_list_uniq.append(current.val)
      print(node_list_uniq)
      ans += 1
    '''
    if current is not None:
    # current and current.left and current.right is not None 
      if str(current.val) not in str_gv:
        str_gv += str(current.val)
        #print(str_gv)
      else:
        if len(str_gv) > max_num:
          max_num = len(str_gv)
          list_len.append(max_num)
        return 
      if current.left is None and current.right is None:
        if len(str_gv) > max_num:
          max_num = len(str_gv)
          list_len.append(max_num)
        #node_set_uniq.clear()

      else:
        helper(current.left, str_gv, list_len, max_num)
        #elif current.right is not None:
        helper(current.right, str_gv, list_len, max_num)

  
  helper(current, "", list_len, max_num)
  return max(list_len) 
   


if __name__=="__main__":
  '''
  # Test Case 1 
  root = Node(1)
  root.left = Node(2)
  root.right = Node(2)
  root.left.left = Node(1)
  root.left.right = Node(2)
  root.right.left = Node(4)
  root.right.right = Node(1)
  '''
  
  '''
  # Test Case 2 
  root = Node(1)
  root.left = Node(2)
  root.left.left = Node(3)
  root.left.right = Node(6)
  root.left.left.left = Node(2)

  root.right = Node(3)
  root.right.left = Node(3)
  root.right.right = Node(1)
  root.right.right.left = Node(5)
  root.right.right.right = Node(6)
  '''
  '''
  # Test Case 3
  root = Node(1)
  root.right = Node(2)
  root.right.left = Node(1)
  root.right.right = Node(1)
  root.right.right.left = Node(4)
  '''
  # Test Case 4
  root = Node(1)
  root.left = Node(2)
  root.left.left = Node(3)
  root.left.left.left = Node(4)
  root.left.left.left.left = Node(5)
  root.left.left.left.left.left = Node(5)
  


  print(find_max_distant_path(root))
