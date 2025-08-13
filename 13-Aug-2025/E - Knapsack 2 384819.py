# Problem: E - Knapsack 2 - https://atcoder.jp/contests/dp/tasks/dp_e

def main():
    N, W = map(int, input().split())
    items = [tuple(map(int, input().split())) for _ in range(N)]
    
    max_value_sum = N * 1000
    INF = 10**18
    dp = [INF] * (max_value_sum + 1)
    dp[0] = 0
    
    for w, v in items:
        for value in range(max_value_sum, v - 1, -1):
            if dp[value - v] + w < dp[value]:
                dp[value] = dp[value - v] + w
    
    answer = 0
    for value in range(max_value_sum + 1):
        if dp[value] <= W:
            answer = value
    print(answer)
    
main()