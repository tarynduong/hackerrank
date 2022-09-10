"""
Given a base-10 integer, n, convert it to binary (base-2).
Then find and print the base-2 integer denoting the maximum number of consecutive 1's in n's binary representation.
When working with different bases, it is common to show the base as a subscript.
"""
import re

if __name__ == '__main__':
  n = int(input().strip())
  remainder = []
  while n > 0:
    remainder.append(n % 2)
    n //= 2
binary = re.sub(r'[^1]', ' ', ''.join(map(str, remainder[::-1]))).split()
max = len(binary[0])
for i in binary:
  if len(i) > max:
    max = len(i)
print(max)
