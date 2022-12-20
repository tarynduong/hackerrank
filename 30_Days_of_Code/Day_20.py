"""
Bubble Sorting algorithm:
for (int i = 0; i < n; i++) {
  // Track number of elements swapped during a single array traversal
  int numberOfSwaps = 0;
  for (int j = 0; j < n - 1; j++) {
    // Swap adjacent elements if they are in decreasing order
    if (a[j] > a[j + 1]) {
      swap(a[j], a[j + 1]);
      numberOfSwaps++;
     }
   }
   // If no elements were swapped during a traversal, array is sorted
   if (numberOfSwaps == 0) {
      break;
   }
}
Task:
Given an array, a, of size n distinct elements, sort the array in ascending order using the Bubble Sort algorithm above. Once sorted, print the following 3 lines:
1. Array is sorted in numSwaps swaps, where numSwaps is the number of swaps that took place.
First Element: firstElement, where  is the first element in the sorted array.
Last Element: lastElement, where  is the last element in the sorted array.
"""
if __name__ == '__main__':
  n = int(input().strip())
  a = list(map(int, input().rstrip().split()))
  
  numSwaps = 0
  for step in range(n - 1, 0, -1):
    for i in range(step):
      if a[i] > a[i + 1]:
        a[i], a[i + 1] = a[i + 1], a[i]
        numSwaps += 1

print('Array is sorted in', numSwaps, 'swaps.')
print('First Element:', a[0])
print('Last Element:', a[-1])
