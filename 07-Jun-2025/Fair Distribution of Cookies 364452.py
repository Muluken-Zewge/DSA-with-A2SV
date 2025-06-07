# Problem: Fair Distribution of Cookies - https://leetcode.com/problems/fair-distribution-of-cookies/

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        bucket = [0] * k
        self.min_unfairness = float('inf')

        def backtrack(i, bucket):
            #base case:all bags are assigned
            if i == len(cookies):
                self.min_unfairness = min(self.min_unfairness, max(bucket))
                return
            
            # Try giving cookies[i] to each child
            for j in range(k):
                bucket[j] += cookies[i]
                # Prune if already worse than current best
                if max(bucket) < self.min_unfairness:
                    backtrack(i + 1, bucket)
                bucket[j] -= cookies[i]
                # Prune redundant assignments to empty buckets
                if bucket[j] == 0:
                    break
        
        backtrack(0,bucket)
        return self.min_unfairness