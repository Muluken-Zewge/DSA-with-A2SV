# Problem: B - Frog 2 - https://atcoder.jp/contests/dp/tasks/dp_b

def main():
  n, k = map(int, input().split())
  h = list(map(int, input().split()))
 
  dp = [0] * n
  for i in range(1,n):
    hi = h[i]
    minimum = float('inf')
    for j in range(max(0,i-k), i):
      hj = h[j]
      minimum = min(minimum, dp[j] + abs(hj-hi))
    dp[i] = minimum
    
  print(dp[n-1])
    
main()