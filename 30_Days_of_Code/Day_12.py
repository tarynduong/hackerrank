"""
Task:
You are given two classes, Person and Student, where Person is the base class and Student is the derived class. 
Completed code for Person and a declaration for Student are provided for you in the editor. 
Observe that Student inherits all the properties of Person.
"""
class Person:
  def __init__(self, firstName, lastName, idNumber):
    self.firstName = firstName
    self.lastName = lastName
    self.idNumber = idNumber
  def printPerson(self):
    print('Name: ', self.lastName + ', ', self.firstName)
    print('ID: ', self.idNumber)

 class Student:
  # Constructor
  def __init__(self, firstName, lastName, idNumber, scores):
    super().__init__(firstName, lastName, idNumber) # inheritance all the methods and properties from the Person class
    self.scores = scores
  # Method to determine the grade letter:
  def calculate_grade(self):
    total = 0
    for i in self.scores:
      total += i
    avg = total / len(self.scores)
    if 90 <= avg <= 100:
      return 'O'
    elif 80 <= avg < 90:
      return 'E'
    elif 70 <= avg < 80:
      return 'A'
    elif 55 <= avg < 70:
      return 'P'
    elif 40 <= avg < 55:
      return 'D'
    elif avg < 40:
      return 'T'
 
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print('Grade: ', s.calculate_grade())
