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
