# Problem: Arithmetic Progression - https://codeforces.com/problemset/problem/382/C

def main():
    n = int(input())
    cards = list(map(int, input().split()))

    if n == 1:
        print(-1)
        return
    cards.sort()
    diffs = [cards[i+1] - cards[i] for i in range(n - 1)]
    unique_diffs = set(diffs)

    if len(unique_diffs) > 2:
        print(0)
        return
    if len(unique_diffs) == 1:
        d = diffs[0]
        result = set()
        result.add(cards[0] - d)  # insert before first
        result.add(cards[-1] + d)  # insert after last
        if n == 2 and d % 2 == 0:
            result.add(cards[0] + d // 2)  # insert in between
        print(len(result))
        print(' '.join(map(str, sorted(result))))
        return

    # Handle case with two differences
    d_small, d_large = sorted(unique_diffs)
    if diffs.count(d_large) != 1 or d_large != 2 * d_small:
        print(0)
        return

    for i in range(n - 1):
        if cards[i+1] - cards[i] == d_large:
            insert = cards[i] + d_small
            print(1)
            print(insert)
            return

    print(0)

main()
