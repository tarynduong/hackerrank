def weightedMean(X, W):
  # Write your code here
  new = [x * w for x, w in zip(X, W)]
  print(round(sum(new) / sum(W), 1))
        
if __name__ == '__main__':
  n = int(input().strip())
  vals = list(map(int, input().rstrip().split()))
  weights = list(map(int, input().rstrip().split()))
  weightedMean(vals, weights)
