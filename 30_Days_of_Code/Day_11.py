# Calculate the hourglass sum for every hourglass in a matrix 6x6, A, then print the maximum hourglass sum.
if __name__ == '__main__':
  arr = []
  arr.append(list(map(int, input().rstrip().split())))
  max = arr[0][0] + arr[0][1] + arr[0][2] + arr[1][1] + arr[2][0] + arr[2][1] + arr[2][2]
  for row in range(len(arr) - 2):
    for col in range(len(arr[0]) - 2):
      hourglass_sum = arr[rol][col] + arr[rol][col + 1] + arr[rol][col + 2] + arr[rol + 1][col + 1] + arr[rol + 2][col] + arr[rol + 2][col + 1] + arr[rol + 2][col + 2]
      if hourglass_sum > max:
        max = hourglass_sum
  print(max)
