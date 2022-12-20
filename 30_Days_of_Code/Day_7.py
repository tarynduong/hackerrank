# Given an array, A, of N integers, print A's elements in reverse order as a single line of space-separated numbers.
if __name__ == '__main__':
  N = int(input().strip()) # the size of an array
  A = list(map(int, input().rstrip().split()))
  print(*A[::-1], sep=' ')
