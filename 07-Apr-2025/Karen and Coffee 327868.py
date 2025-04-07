# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

def main():
    n, k, q = map(int, input().split())
    MAX_TEMP = 200001
    diff = [0] * (MAX_TEMP + 1)
    
    # Difference array for range updates
    for _ in range(n):
        l, r = map(int, input().split())
        diff[l] += 1
        if r + 1 < MAX_TEMP:
            diff[r + 1] -= 1
    
    # Prefix sum to get frequency at each temperature
    freq = [0] * MAX_TEMP
    freq[0] = diff[0]
    for i in range(1, MAX_TEMP):
        freq[i] = freq[i - 1] + diff[i]
            
    
    # Mark admissible temperatures (freq[i] >= k)
    admissible = [0] * MAX_TEMP
    for i in range(MAX_TEMP):
        admissible[i] = 1 if freq[i] >= k else 0
        
    # Prefix sum over admissible[] to answer queries quickly
    admissible_prefix = [0] * MAX_TEMP
    admissible_prefix[0] = admissible[0]
    for i in range(1, MAX_TEMP):
        admissible_prefix[i] = admissible_prefix[i - 1] + admissible[i]
        
    for _ in range(q):
        a, b = map(int, input().split())
        result = admissible_prefix[b] - admissible_prefix[a - 1]
        print(result)
        
main()