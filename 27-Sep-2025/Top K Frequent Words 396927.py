# Problem: Top K Frequent Words - https://leetcode.com/problems/top-k-frequent-words/

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = Counter(words)
        sorted_words = sorted(freq.keys(), key=lambda w: (-freq[w], w))
        return sorted_words[:k]