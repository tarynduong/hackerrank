# Stack: LIFO - Last In First Out; Queue: FIFO - First In First Out
# Write a program to check a word is a palindrome or not.
# A palindrome is a word, phrase, number, or other sequence of characters which reads the same backwards and forwards. 
class Solution:
  def __init__(self):
    self.stack = []
    self.queue = []
  def enqueueCharacter(self, char):
    self.queue.append(char)
  def pushCharacter(self, char):
    self.stack.append(char)
  def dequeueCharacter(self):
    return self.queue.pop(0)
  def popCharacter(self):
    return self.stack.pop
  
s = input()
obj = Solution()
for i in range(len(s)):
  obj.pushCharacter(s[i])
  obj.enqueueCharacter(s[i])
isPalindrome = True
# Idea: pop the top character from stack, dequeue the first character from queue, then compare both the characters
for i in range(len(s) // 2):
  if obj.popCharacter() != obj.dequeueCharacter():
    isPalindrome = False
    break
if isPalindrome:
  print('The word ', s, ' is a palindrome.')
else:
  print('The word ', s, ' is not a palindrome.')
