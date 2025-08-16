# Problem: H - Grid 1 - https://atcoder.jp/contests/dp/tasks/dp_h

def main():
  MOD = 10**9 + 7
  r, c = map(int, input().split())
  arr = []
  for _ in range(r):
    curr_row = list(input())
    arr.append(curr_row)
    
  dp = [[0] * c for _ in range(r)]
  dp[0][0] = 1
  for i in range(r):
    for j in range(c):
      if (i - 1 >= 0 and arr[i-1][j] != '#') and (j - 1 >= 0 and arr[i][j-1] != '#'):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
      elif i - 1 >= 0 and arr[i-1][j] != '#':
        dp[i][j] = dp[i-1][j]
      elif j - 1 >= 0 and arr[i][j-1] != '#':
        dp[i][j] = dp[i][j-1]
        
  return dp[r-1][c-1] % MOD
    
print(main())