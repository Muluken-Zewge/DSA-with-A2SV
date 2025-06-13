# Problem: Cities and Roads - https://www.eolymp.com/en/contests/9060/problems/78597

def main():
    n = int(input())
    roads = 0
    for i in range(n):
        row = list(map(int, input().split()))
        for j in range(len(row)):
            if row[j] == 1:
                roads += 1
    
    print(roads//2)

main()