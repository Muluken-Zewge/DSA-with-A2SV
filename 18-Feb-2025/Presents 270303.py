# Problem: Presents - https://codeforces.com/problemset/problem/136/A

def main():
    num_of_friends = int(input())
    
    p = list(map(int, input().split()))
    n = [0] * len(p)
    
    for i in range(len(p)):
        n[p[i] -1] = i + 1 
    
    for num in n:
        print(num, end=" ")
    
main()