# Problem: Combination Sum - https://leetcode.com/problems/combination-sum/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def backtrack(start: int, path: List[int]):
        # Base case: combination complete
            if len(path) == k:
                ans.append(path[:])
                return

        # Try numbers from 'start' to 'n'
            for num in range(start, n + 1):
                path.append(num)          # choose i
                backtrack(num + 1, path)  # explore further
                path.pop()              # backtrack
        
        ans = []
        backtrack(1 , [])

        return ans