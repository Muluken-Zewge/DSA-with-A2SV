# Problem: Kefa and Company - https://codeforces.com/problemset/problem/580/B

def main():
    n, d = map(int, input().split())
    friends = []
    for _ in range(n):
        m, s = map(int, input().split())
        friends.append([m,s])

    friends.sort()
    current_friend_factor = 0
    max_friend_factor = 0
    left = 0 

    for right in range(len(friends)):
        current_friend_factor += friends[right][1]

        while friends[right][0] - friends[left][0] >= d:
            current_friend_factor -= friends[left][1]
            left += 1

        max_friend_factor = max(max_friend_factor, current_friend_factor)

    print(max_friend_factor)

main()
