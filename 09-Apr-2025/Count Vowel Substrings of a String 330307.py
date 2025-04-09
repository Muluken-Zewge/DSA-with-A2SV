# Problem: Count Vowel Substrings of a String - https://leetcode.com/problems/count-vowel-substrings-of-a-string/description/

from collections import defaultdict
class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = {'a':1,'e':1, 'i':1, 'o': 1, 'u': 1}
        vowel_substrings = 0
        for i in range(len(word)):
            if word[i] not in vowels:
                continue
            vowel_map = defaultdict(int)
            for j in range(i, len(word)):
                if word[j] in vowels:
                    vowel_map[word[j]] += 1
                else:
                    break
                if all(vowel_map[char] > 0 for char in vowels):
                        vowel_substrings += 1
        
        return vowel_substrings
        