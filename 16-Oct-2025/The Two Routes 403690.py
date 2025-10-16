# Problem: The Two Routes - https://codeforces.com/problemset/problem/601/A

from collections import deque

def bfs(start, graph, n):
    dist = [-1] * (n + 1)
    q = deque([start])
    dist[start] = 0
    while q:
        u = q.popleft()
        for v in graph[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
    return dist[n]

def solve():
    n, m = map(int, input().split())
    rail = [set() for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        rail[u].add(v)
        rail[v].add(u)
    
    # Build the road (complement) graph
    road = [set() for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j and j not in rail[i]:
                road[i].add(j)
    
    # Check if 1 and n are connected by railway
    connected_by_rail = n in rail[1]
    
    if connected_by_rail:
        dist_train = bfs(1, rail, n)
        dist_bus = bfs(1, road, n)
    else:
        dist_train = bfs(1, road, n)
        dist_bus = bfs(1, rail, n)
    
    if dist_train == -1 or dist_bus == -1:
        print(-1)
    else:
        print(max(dist_train, dist_bus))

solve()