# Problem: Relative Sort Array
(Easy) - https://leetcode.com/problems/relative-sort-array/

from collections import Counter
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = Counter(arr1) #store number of occurances in arr1
        ans = []

        for num in arr2:
            for _ in range(count[num]):
                ans.append(num)

        remaining = [num for num in arr1 if num not in arr2]
        ans.extend(sorted(remaining))

        return ans