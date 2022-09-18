# Write a program to return the sum of all divisors of an integer, n
# Interface
class AdvancedArithmetic(object):
  # Method declaration for the abstract
  def divisorSum(n):
    raise NotImplementedError
# Class that implements the interface
class Calculator(AdvancedArithmetic):
  def divisorSum(self, n):
    val = 0
    for i in range(1, n + 1):
      if n % i == 0:
        val += i
    return val
 
n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print('I implemented: ', type(my_calculator).__bases__[0].__name__)
print(s)
