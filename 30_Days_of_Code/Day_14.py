"""
Write a Difference class that has a private integer array (elements) for storing N non-negative integers, and a public integer (maximumDifference) for storing
the maximum absolute difference.
"""
class Difference:
  # Constructor that takes an array of integers, A, as a parameter and saves it to the __elements instance variable
  def __init__(self, A):
    self.__elements = A
  # Method that finds the maximum absolute difference between any 2 numbers in __elements and stores it in the maximumDifference instance variable
  def computeDifference(self):
    max = 0
    for i in range(len(self.__elements)):
      for j in range(len(self.__elements)):
        absolute = abs(__elements[i] - __elements[j])
        if absolute > max:
          max = absolute
    self.maximumDifference = max
  
  _ = input()
  a = [int(e) for e in input().split(' ')]
  d = Difference(a)
  d.computeDifference()
  print(d.maximumDifference)
