""" A level-order traversal, also known as a breadth-first search, visits each level of a tree's nodes from left to right, top to bottom.
Write the levelOrder function to print the level-order traversal of the binary search tree."""
class Node:
  def __init__(self, data):
    self.right = self.left = None
    self.data = data

class Solution:
  def insert(self, data, root):
    if root == None:
      return Node(data)
    else:
      if data <= root.data:
        cur = self.insert(root.left, data)
        root.left = cur
      else:
        cur = self.insert(root.right, data)
        root.right = cur
    return root
  
  def levelOrder(self.root):
    nodes_queue = []
    data_list = []
    temp_node = root
    while temp_node:
      data_list.append(temp_node.data)
      if temp_node.left is not None:
        nodes_queue.append(temp_node.left)
      elif temp_node.right is not None:
        nodes_queue.append(temp_node.right)
      elif len(nodes_queue) == 0:
        break
      temp_node = nodes_queue.pop(0)
    print(' '.join(list(map(str, data_list))))

T = int(input())
root = None
for i in range(T):
  data = int(input())
  root = Solution().insert(root, data)
Solution().levelOrder(root)
