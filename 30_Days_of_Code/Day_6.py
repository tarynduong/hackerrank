"""
Task:
Given a string, S, print its even-indexed and odd-indexed characters as 2 space-separated strings on a single line.
E.g. abcdef => ace bdf
The first line contains an integer, T (the number of test cases). Each line i of the T subsequent lines contain a string, S.
"""
T = int(input())
for i in range(T):
  S = str(input())
  print(S[::2] + ' ' + S[1::2])
