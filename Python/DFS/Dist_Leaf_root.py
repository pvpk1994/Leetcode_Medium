# Distances between root Node and leaf node
# Author: Pavan Kumar Paluri

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def max_dist_leaf_root(root:Node):
  stack = []
  dist = []
  current = root
  def helper(current:Node):
    if current is None:
      return
    if current is not None:
      # current
      stack.append(current.val)
      if current.left is None and current.right is None:
        # leaf node
        dist.append(len(stack)-1)
      if current.left is not None:
        helper(current.left)
      if current.right is not None:
        helper(current.right)
      stack.pop()
  helper(current)
  print(dist)
      
if __name__ == "__main__":
  root = Node(1)
  n1= root.left = Node(3)
  n5 =n1.right = Node(4)
  n6 = n5.left = Node(6)
  n7 = n5.right = Node(9)
  n2= n1.left = Node(5)
  n3= n2.left = Node(7)
  n4 = n3.left = Node(8)
  n8 = root.right = Node(5)
  n9 = n8.left = Node(7)
  n10 = n8.right = Node(6)
  max_dist_leaf_root(root)
