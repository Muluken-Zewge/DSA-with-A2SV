# Problem: Keyboard Row - https://leetcode.com/problems/keyboard-row/description/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        #store the row of chars in a dict with the chars in a set for fast lookup
        rows = {
            1: set("qwertyuiop"),
            2: set("asdfghjkl"),
            3: set("zxcvbnm"),
        }
        same_row_words = []

        for word in words:
            all_chars_in_row = True #assume all chars are in the same row

            #determine in which row the first char of each word belongs
            for row_num, chars in rows.items():
                if word.lower()[0] in chars:
                    word_row = row_num
                    break
            
            #check if the rest of the chars are in the same row
            for char in word.lower():
                if char not in rows[word_row]:
                    all_chars_in_row = False
                    break
            
            #append words with all chars in the same row
            if all_chars_in_row:
                same_row_words.append(word)

        return same_row_words