# Problem: Same Differences - https://codeforces.com/problemset/problem/1520/D

def main():
    test_cases = int(input())

    for _ in range(test_cases):
        n = int(input())
        a = list(map(int, input().split()))
        
        # Create the b array where b[i] = a[i] - (i + 1)
        b = [a[i] - (i + 1) for i in range(n)]
        
        # Use a frequency map to count occurrences of each value in b
        freq = {}
        for num in b:
            freq[num] = freq.get(num, 0) + 1
        
        # Calculate the number of valid pairs
        result = 0
        for count in freq.values():
            if count >= 2:
                result += count * (count - 1) // 2
        
        print(result)

main()