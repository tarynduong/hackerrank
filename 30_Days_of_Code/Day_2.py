import math

# Complete the 'solve' function below.
""" The function accepts following parameters:
1. DOUBLE meal_cost
2. INTEGER tip_percent
3. INTEGER tax_percent
Task: find and print the meal's total cost. Round the result to the nearest integer.
"""

def solve(meal_cost, tip_percent, tax_percent):
  # Write your code here
  total = meal_cost*(1 + tip_percent/100 + tax_percent/100)
  if total - int(total) < .5:
    print(math.floor(total))
  else:
    print(math.ceil(total))

if __name__ == '__main__':
  meal_cost = float(input().strip())
  tip_percent = int(input().strip())
  tax_percent = int(input().strip())
  solve(meal_cost, tip_percent, tax_percent)
