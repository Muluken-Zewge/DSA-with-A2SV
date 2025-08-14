# Problem: G - Longest Path - https://atcoder.jp/contests/dp/tasks/dp_g

from collections import deque

def main():
    N, M = map(int, input().split())
    adj = [[] for _ in range(N)]
    indegree = [0] * N
    
    for _ in range(M):
        x, y = map(int, input().split())
        adj[x - 1].append(y - 1)
        indegree[y - 1] += 1
    
    # Topological sort
    q = deque([i for i in range(N) if indegree[i] == 0])
    dp = [0] * N
    
    while q:
        u = q.popleft()
        for v in adj[u]:
            if dp[u] + 1 > dp[v]:
                dp[v] = dp[u] + 1
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)
    
    print(max(dp))
    
main()