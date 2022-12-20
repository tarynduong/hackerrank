""" A Node object has an integer data field, data, and a Node instance pointer, next, pointing to another node (i.e.: the next node in a list).
A removeDuplicates function takes a pointer to the  node of a linked list as a parameter.
Write the removeDuplicates function to delete any duplicate nodes from the list and returns the head of the updated list."""
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None 

class Solution:
  def insert(self, head, data):
    p = Node(data)           
    if head == None:
      head = p
    elif head.next == None:
      head.next = p
    else:
      start = head
      while(start.next != None):
        start = start.next
        start.next = p
    return head  
  
  def display(self, head):
    current = head
    while current:
      print(current.data, end = ' ')
      current = current.next
  
  def removeDuplicates(self, head):
    if head is None:
      return head
        values = [head.data]
        temp = head.next
        prev = head
        while temp:
            if temp.data in values:
                temp = temp.next
            else:
                values.append(temp.data)
                prev.next = temp
                prev = prev.next
                temp = temp.next
        prev.next = None
        return head

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
head=mylist.removeDuplicates(head)
mylist.display(head); 

