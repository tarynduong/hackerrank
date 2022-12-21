""" Given the expected and actual return dates for a library book, create a program that calculates the fine (if any).
The fee structure is as follows:
If the book is returned on or before the expected return date, no fine will be charged.
If the book is returned after the expected return day but still within the same calendar month and year as the expected return date, fine = 15 x number of days late.
If the book is returned after the expected return month but still within the same calendar year as the expected return date, fine = 500 x number of months late.
If the book is returned after the calendar year in which it was expected, there is a fixed fine of 10000 Hackos."""
d1, m1, y1 = map(int, input().split())
d2, m2, y2 = map(int, input().split())

if y1 < y2:
  fine = 0
elif y1 == y2:
  if m1 > m2:
    fine = (m1 - m2) * 500
  else:
    if d1 > d2:
      fine = (d1 - d2) * 15
    else:
      fine = 0
else:
  fine = 10000
print(fine)
