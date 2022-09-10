# Recursive Method for Calculating Factorial
import os

def factorial(n):
  if n <= 1:
    return 1
  else:
    return n * factorial(n - 1)

if __name__ == '__main__':
  fptr = open(os.environ['OUTPUT_PATH'], 'w') # os.environ lets you access environment variables named OUTPUT_PATH from your python script
  # fptr now is a file pointer, if you change it to fptr = sys.stdout, it becomes an open stream
  # simply change the path of the python code os.environ['OUTPUT_PATH'] to your local path if you write code on your local IDE
  n = int(input().strip())
  result = factorial(n)
  fptr.write(str(result) + '\n')
  fptr.close()
