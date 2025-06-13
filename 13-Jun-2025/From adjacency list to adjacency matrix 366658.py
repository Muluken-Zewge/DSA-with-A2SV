# Problem: From adjacency list to adjacency matrix - https://basecamp.eolymp.com/en/problems/3982

def main():
    n = int(input())
    matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        edges = list(map(int, input().split()))
        for j in range(1, edges[0]+1):
            matrix[i][edges[j]-1] = 1

    for k in range(n):
        print(*matrix[k])

main()