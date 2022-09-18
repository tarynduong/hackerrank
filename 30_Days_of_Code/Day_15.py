# A Node object has an integer data field, data, and a Node instance pointer, next, pointing to the next node in the list
# The head argument is null for an empty list.
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    
class Solution:
  def display(self, head):
    current = head
    while current:
      print(current.data, end = ' ')
      current = current.next
  """ Insert function has two parameters: a pointer, head, pointing to the first node of a linked list, and an integer, data, that must be added to the end of the list
  as a new Node object. Once the new node is added, return the reference to the head node."""
  def insert(self, head, data):
    temp = Node(data)
    if head is None:
      head = temp
      return head
    current = head
    while current.next is not None:
      current = current.next
    current.next = temp
    return head
 
myList = Solution()
head = None
for i in range(int(input())):
  data = int(input())
  head = myList.insert(head, data)
myList.display(head)
