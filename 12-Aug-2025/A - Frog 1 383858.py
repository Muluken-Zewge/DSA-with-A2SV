# Problem: A - Frog 1 - https://atcoder.jp/contests/dp/tasks/dp_a

def main():
  n = int(input())
  h = list(map(int, input().split()))
  
  dp = [0] * n
  for i in range(1,n):
    one_step = dp[i-1] + abs(h[i] - h[i-1])
    dp[i] = one_step
    if i - 2 >= 0:
      two_step = dp[i-2] + abs(h[i] - h[i-2])
      dp[i] = min(one_step, two_step)
      
  return dp[n-1]
  
print(main())