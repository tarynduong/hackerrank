# Given an array, A, of N integers, print A's elements in reverse order as a single line of space-separated numbers.
if __name__ == '__main__':
  N = int(input().strip()) # the size of an array
  A = list(map(int, input().rstrip().split())) # enter integers as array's elements, for split() by default any whitespace is a separator
  print(*A[::-1], sep=' ') # with * the output will be in the form of a sequence of integers
