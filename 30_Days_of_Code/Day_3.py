"""
Given an integer, , perform the following conditional actions:
If  is odd, print Weird
If  is even and in the inclusive range of 2 to 5, print Not Weird
If  is even and in the inclusive range of 6 to 20, print Weird
If  is even and greater than 20, print Not Weird
Complete the stub code provided in your editor to print whether or not  is weird.
"""
if __name__ == '__main__':
  n = int(input().strip())
  if n % 2 != 0:
    print('Weird')
  elif n % 2 == 0:
    if 6 <= n <= 20:
      print('Weird')
    elif 2 <= n <= 5 or n > 20:
      print('Not Weird')
