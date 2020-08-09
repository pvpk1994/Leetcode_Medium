# Author: Pavan Kumar Paluri
# Find max Root-to-leaf path with distant nodes
# Naive approach: Cover all root-to-leaf paths and return max count of distant nodes.
import math
class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

class Solution:
  def __init__(self):
    self.max = -math.inf
    self.node_stack = []
    self.counter = 0
    self.list_max = []

  def max_distant_nodes(self, root: Node):
    # Pre-order traversal
    if root is None:
      return
    if root.val not in self.node_stack:
      self.node_stack.append(root.val)
    else:
      self.list_max.append(len(self.node_stack))
      # print(self.node_stack)
      self.node_stack.pop() 
      return
    if root.left is None and root.right is None:
      # end of branch
      self.list_max.append(len(self.node_stack))
      print(self.node_stack)
      self.node_stack.pop()
      return 
    self.max_distant_nodes(root.left)
    self.max_distant_nodes(root.right)
    # self.node_stack.pop() 


  def print_result(self):
    print("Max-Dist nodes are: " + str(max(self.list_max)))

if __name__ == "__main__":
  '''
  root = Node(1)
  root.left = Node(2)
  root.right = Node(3)
  root.right.left = Node(6)
  root.right.right = Node(3)
  '''
  '''
  # Test-Case-2:
  root = Node(1)
  root.left = Node(2)
  root.left.left = Node(3)
  root.left.left.left = Node(1)
  root.left.right = Node(4)
  root.left.right.left = Node(6)
  root.right = Node(5)
  root.right.right = Node(5)
  root.right.right.left = Node(4)
  '''

  # Interview Test-cases
  '''
  root = Node(1)
  root.left = Node(2)
  root.left.left = Node(1)
  root.left.right = Node(2)

  root.right = Node(2)
  root.right.left = Node(4)
  root.right.right = Node(1)
  '''

  root = Node(1)
  root.right = Node(2)
  root.right.left = Node(1)
  root.right.right = Node(1)
  root.right.right.left = Node(4)

  sol = Solution()
  sol.max_distant_nodes(root)
  sol.print_result()

