""" The height of a binary search tree is the number of edges between the tree's root and its furthest leaf.
Write the getHeight function to return the height of the binary search tree."""
class Node:
  def __init__(self, data):
    self.right = self.left = None
    self.data = data
    
class Solution:
  def insert(self, root, data):
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
  
  def getHeight(self, root):
    if root != None:
      left_height = self.getHeight(root.left) + 1
      right_height = self.getHeight(root.right) + 1
      return max(left_height, right_height)
    else:
      return -1

T = int(input())
root = None
for i in range(T):
  data = int(input())
  root = Solution().insert(root, data)
print(Solution().getHeight(root))
