# Problem: Majority Element - https://leetcode.com/problems/majority-element/description/

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        occurence_table = {} #to store the nums and their occurences

        for num in nums:
            if num not in occurence_table: #check if num doesn't exist in the table
                occurence_table[num] = 1
            else:
                occurence_table[num] += 1 #increment its value by 1 if it exists

        #use key parameter to compare values instead of keys
        majority_element = max(occurence_table, key=occurence_table.get)

        return majority_element
        