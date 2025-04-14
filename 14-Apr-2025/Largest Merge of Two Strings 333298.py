# Problem: Largest Merge of Two Strings - https://leetcode.com/problems/largest-merge-of-two-strings/

class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        merge = ''
        w1 = 0
        w2 = 0
    
        while w1 < len(word1) and w2 < len(word2):
            #compare each string(not a single char) after removing a char from one of them in each iteration
            if word1[w1:] > word2[w2:]:
                merge += word1[w1]
                w1 += 1
            else:
                merge += word2[w2]
                w2 += 1

        merge += word1[w1:]
        merge += word2[w2:]

        return merge