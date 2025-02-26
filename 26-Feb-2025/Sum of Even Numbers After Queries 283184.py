# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        answer = []
        #to store sum of even nums before doing the calculation of the query
        saved_sum = sum(num for num in nums if num % 2 == 0)

        for query in queries:
            #check if the num under consideration is even
            if nums[query[1]] % 2 == 0:
                saved_sum -= nums[query[1]] #it should not be added since calculation will be done on it
            
            #do the calculation
            nums[query[1]] += query[0]

            #if it is even after the calculaton, add it
            if nums[query[1]] % 2 == 0:
                saved_sum += nums[query[1]]
            
            #append to the answer list
            answer.append(saved_sum)

        return answer