# Problem: Find the Index of the First Occurrence in a String - https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Rabin-Karp Algorithm
        MOD = 10**9 + 7
        base = 27

        def convert(char):
            return ord(char) - 96
       
        def add_last(Hash, char):
            return (Hash * base + convert(char)) % MOD
       
        def poll_first(Hash, char, base_power):
            return (Hash - convert(char) * base_power) % MOD
        
        N1, N2 = len(haystack), len(needle)
        if N1 < N2:
            return -1
       
        # Precompute base powers mod MOD
        base_powers = [1] * (N2 + 1)
        for i in range(1, N2 + 1):
            base_powers[i] = (base_powers[i - 1] * base) % MOD
       
        target = window_hash = 0
        # Calculate the hash of the needle and the initial window in haystack
        for char in needle:
            target = add_last(target, char)
           
        for i in range(N2):
            window_hash = add_last(window_hash, haystack[i])

        if window_hash == target:
            # Verify the actual substring matches
            if haystack[:N2] == needle:
                return 0
           
        # Slide the window over the haystack
        for right in range(N2, N1):
            left = right - N2
            window_hash = add_last(window_hash, haystack[right])
            window_hash = poll_first(window_hash, haystack[left], base_powers[N2])
            if window_hash == target:
                # Verify the actual substring matches
                if haystack[left+1:right+1] == needle:
                    return right - N2 + 1
           
        return -1
