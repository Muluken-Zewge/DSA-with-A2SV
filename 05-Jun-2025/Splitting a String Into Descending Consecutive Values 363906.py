# Problem: Splitting a String Into Descending Consecutive Values - https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

class Solution:
    def splitString(self, s: str) -> bool:
        def backtrack(i, path):
        # Base case: if we reach the end of the string
        # and have at least two numbers in the sequence
            if i == len(s):
                return len(path) >= 2
            
            # Try every possible substring starting at index i
            for j in range(i + 1, len(s) + 1):
                num = int(s[i:j])
        # If this is the first number or it continues a descending-by-1 pattern
                if not path or num == path[-1] - 1:
                    # Choose: add the number to the current path
                    path.append(num)

                # Explore: continue building the sequence from the next index
                    if backtrack(j, path):
                        return True # Valid sequence found
                    # backtrack: remove the last number and try other options
                    path.pop()

            # If no valid sequence found from this state, return False        
            return False

        return backtrack(0, [])