# Read a string, S, and print its integer value; if S cannot be converted to an integer, print Bad String.
try:
  print(int(input()))
except ValueError:
  print('Bad String')
