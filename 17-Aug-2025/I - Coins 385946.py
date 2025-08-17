# Problem: I - Coins - https://atcoder.jp/contests/dp/tasks/dp_i

def main():
  N = int(input())
  probs = list(map(float, (input().split())))
  
  dp = [[0.0] * (N + 1) for _ in range(N + 1)]
  dp[0][0] = 1.0  # base case

  for i in range(1, N + 1):
      p = probs[i - 1]
      for j in range(0, i + 1):
          # If coin i is head
          if j > 0:
              dp[i][j] += dp[i - 1][j - 1] * p
          # If coin i is tail
          dp[i][j] += dp[i - 1][j] * (1 - p)

  # More heads than tails
  need = N // 2 + 1
  ans = sum(dp[N][need:])
  
  return ans
    
print(main())