# Problem: Number of Matching Subsequences - https://leetcode.com/problems/number-of-matching-subsequences/

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        buckets = defaultdict(deque)
        
        # group words by first char
        for w in words:
            buckets[w[0]].append(w)
        
        count = 0
        
        # process characters of s
        for ch in s:
            queue = buckets[ch]
            for _ in range(len(queue)):
                word = queue.popleft()
                if len(word) == 1:   # fully matched
                    count += 1
                else:
                    # push the remainder of word into bucket of its next needed char
                    buckets[word[1]].append(word[1:])
        
        return count
