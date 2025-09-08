# Problem: Remove Smallest - https://codeforces.com/problemset/problem/1399/A

def main():
    
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        a.sort()
        is_possible = True
        
        for i in range(n-1):
            if a[i+1] - a[i] > 1:
                 is_possible = False
            
        if (is_possible):
            print("YES")
        else:
            print("NO")

main()