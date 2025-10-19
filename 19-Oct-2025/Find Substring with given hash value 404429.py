# Problem: Find Substring with given hash value - https://leetcode.com/problems/find-substring-with-given-hash-value/description/

class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        n = len(s)
        power_k = pow(power, k, modulo)
        current_hash = 0
        result_index = 0

        # We'll traverse from right to left
        for i in range(n - 1, -1, -1):
            val = ord(s[i]) - 96  # 'a' -> 1, ..., 'z' -> 26
            current_hash = (current_hash * power + val) % modulo

            # Maintain window size k
            if i + k < n:
                remove_val = (ord(s[i + k]) - 96) * power_k % modulo
                current_hash = (current_hash - remove_val) % modulo

            # Check if hash matches
            if n - i >= k and current_hash == hashValue:
                result_index = i  # store the earliest (leftmost) valid index

        return s[result_index:result_index + k]        