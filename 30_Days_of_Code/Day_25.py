# Check whether an integer is a prime by using an algorithm with O(sqrt(n))
import math
T = int(input())
for t in range(T):
  n = int(input())
  count = 0
  if n < 2:
    print('Not prime')
  else:
    for i in range(1, int(math.sqrt(n)) + 1):
      if n % i == 0:
        count += 1
    if count < 2:
      print('Prime')
    else:
      print('Not prime')
