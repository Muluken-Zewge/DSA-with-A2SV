# Problem: Find Words That Can Be Formed by Characters - https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        len_of_good = 0

        for word in words:
            is_good = True
            for char in word:
                if chars.count(char) < word.count(char):
                    is_good = False
                    break
            if is_good:
                len_of_good += len(word)
        
        return len_of_good
    