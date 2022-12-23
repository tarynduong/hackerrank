""" Given a set S = {1, 2, 3, ..., N}. Find 2 integers A and B, where A < B, from set S such that A&B is the maximum possible and also less than a given integer, K.
In this case, & represents the bitwise and operator.
Idea:
- 𝐴 & 𝐵 will never be greater than 𝐴 nor than 𝐵
- If we have a solution 𝐶, then both 𝐴 and 𝐵 should have the same 1-bit as 𝐶 has, including possibly a few more.
- The least possible value for 𝐵 is then to set a 1-bit at the least bit in 𝐴 that is still 0.
- If this 𝐵 is still not greater than 𝑁, then we can conclude that 𝐶 is a solution.
- With the above steps in mind, it makes sense to first try with the greatest 𝐶 possible, i.e. 𝐶=𝐾−1, and then reduce 𝐶 until the above routine finds a 𝐵 that
is not greater than 𝑁."""
jmport os
def bitwiseAnd(N, K):
  for A in range(K-1, 0, -1):
    # Find the least bit that has a zero in this number A
    bit = (A + 1) & -(A + 1)
    B = A + bit
    if B <= N:
      return A
  return 0

if __name__ == '__main__':
  fptr = open(os.environ['OUTPUT_PATH'], 'w')
  t = int(input().strip())
  for t_itr in range(t):
    first_multiple_input = intput().rstrip().split()
    count = int(first_multiple_input[0])
    lim = int(first_multiple_input[1])
    res = bitwiseAnd(count, lim)
    fptr.write(str(res) + '\n')
  fptr.close()
