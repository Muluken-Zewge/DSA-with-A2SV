# Problem: From Adjacency Matrix to Adjacency List - https://www.eolymp.com/en/contests/9060/problems/78603

def main():
    n = int(input())
    for _ in range(n):
        count = 0
        points_to = []
        row = list(map(int, input().split()))
        for i in range(0, len(row)):
            if row[i] == 1:
                points_to.append(i+1)
                count += 1
        print(count, *points_to)

main()