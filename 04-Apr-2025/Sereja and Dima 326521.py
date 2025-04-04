# Problem: Sereja and Dima - https://codeforces.com/problemset/problem/381/A

def main():
    n = int(input())
    cards = list(map(int, input().split()))
    
    sereja = 0
    dima = 0
    left = 0
    right = n - 1
    turn = 0  # 0 for Sereja, 1 for Dima
 
    while left <= right:
        if cards[left] > cards[right]:
            chosen = cards[left]
            left += 1
        else:
            chosen = cards[right]
            right -= 1
 
        if turn % 2 == 0:
            sereja += chosen
        else:
            dima += chosen
 
        turn += 1
 
    print(sereja, dima)
 
main()