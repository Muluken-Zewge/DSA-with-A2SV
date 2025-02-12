# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}  #empty dict to store anagrams
        for word in strs:
            #sort word to store it as key in anagrams
            sorted_word = ''.join(sorted(word))
#if not in anagrams,create a key with sorted_word and store the original word as a value 
            if sorted_word not in anagrams: 
                anagrams[sorted_word] = [word]
            else: #if in anagrams, append word to the list
                anagrams[sorted_word].append(word)
        
        anagram_list = list(anagrams.values())

        return anagram_list
