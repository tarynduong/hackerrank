"""
Abstract Method (AM)
>> Definition: AM is a method that is declared, but contains no implementation. Abstract classes cannot be instantiated, and require subclasses to provide implementations
for the AM.
>> Why using AM?
- It helps hide irrelevant details from the user to focus only on the essential details to increase efficiency, thereby reducing complexity
- In Python, abstract base classes provide a blueprint for concrete classes. They don't contain implementation. Instead, they provide an interface and make sure that
derived concrete classes are properly implemented. 
"""
from abc import ABCMeta, abstractmethod

class Book(object, metaclass = ABCMeta):
  def __init__(self, title, author):
    self.title = title
    self.author = author
  @abstractmethod
  def display():
    pass

class MyBook(Book):
  def __init__(self, title, author, price):
    super().__init__(title, author)
    self.price = price
  def display(self):
    print('Title:', self.title, '\nAuthor:', self.author, '\nPrice:', self.price)
 
title = input()
author = input()
price = int(input())
new_book = MyBook(title, author, price)
new_book.display()
