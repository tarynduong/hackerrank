# Given an integer, n, print its first 10 multiples. Each multiple nxi (where 1 <= i <= 10) should be printed on a new line in the form: n x i = result.
if __name__ == '__main__':
  n = int(input().strip())
  for i in range(1, 11, 1):
    print(f'{n} x {i} = {n * i}')
