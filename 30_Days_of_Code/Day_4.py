# Write a Person class with an instance variable, age.
class Person:
  # A constructor that takes an integer, initialAge, as a parameter
  def __init__(self, initialAge):
    # Checks that initialAge is not negative
    if initialAge < 0:
      print('Age is not valid, setting age to 0.')
      self.age = 0
    else:
      self.age = initialAge
  # Write other instance methods
  def amIOld(self):
    if self.age < 13:
      print('You are young.')
    elif 13 <= self.age < 18:
      print('You are a teenager.')
    else:
      print('You are old.')
  def yearPasses(self):
    self.age += 1;

# Check class
t = int(input()) # t is the number of test cases
for i in range(0, t):
  age = int(input())         
  p = Person(age)  
  p.amIOld()
  for j in range(0, 3):
    p.yearPasses()       
  p.amIOld()
  print("")

"""
Test Case 0: initialAge = -1
Because initialAge < 0, our code must set age to 0 and print "Age is not valid..." message followed by the young message. Three years pass and age = 3,
so we print the young message again.

Test Case 1: initialAge = 10
Because initialAge < 13, our code should print that the person is young. Three years pass and age = 16, so we print that the person is now a teenager.

Test Case 2: initialAge = 16
Because initialAge in range of 13 and 18, our code should print that the person is a teenager. Three years pass and age = 19, so we print that the person is old.

Test Case 3: initialAge = 18
Because initialAge >= 18, our code should print that the person is old. Three years pass and the person is still old at age = 21, so we print the old message again.
