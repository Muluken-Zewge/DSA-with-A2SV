# Problem: Regular Graph - https://basecamp.eolymp.com/en/problems/5076

from collections import defaultdict
def main():
    n, m = map(int, input().split())
    counter = defaultdict(int)
    for _ in range(m):
        x, y = map(int, input().split())
        counter[x] += 1
        counter[y] += 1
    # Ensure all nodes from 1 to n are represented
    for i in range(1, n + 1):
        _ = counter[i]
    if len(set(counter.values())) == 1:
        print("YES")
    else:
        print("NO")
main()