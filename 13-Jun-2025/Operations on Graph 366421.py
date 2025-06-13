# Problem: Operations on Graph - https://www.eolymp.com/en/contests/9060/problems/78602

from collections import defaultdict
def main():
    graph = defaultdict(list)
    def addEdge(u,v):
        graph[u].append(v)
        graph[v].append(u)
    def vertex(u):
        if len(graph[u]) > 0:
            print(*graph[u])
    
    n = int(input())
    k = int(input())
    for _ in range(k):
        oper = list(map(int, input().split()))
        if oper[0] == 1:
            addEdge(oper[1],oper[2])
        else:
            vertex(oper[1])

main()