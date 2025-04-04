# Problem: Smallest Value of the Rearranged Number - https://leetcode.com/problems/smallest-value-of-the-rearranged-number/description/

class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0  # Special case: If num is zero, return zero directly
    
        is_negative = num < 0
        digits = list(str(abs(num)))  # Extract digits as a list of characters

        if is_negative:
            # Sort in descending order for negative numbers
            digits.sort(reverse=True)
        else:
            # Sort in ascending order for positive numbers
            digits.sort()
            
            # If first digit is '0', swap with first non-zero digit
            if digits[0] == '0':
                for i in range(1, len(digits)):
                    if digits[i] != '0':  
                        digits[0], digits[i] = digits[i], digits[0]
                        break

        # Reconstruct the number
        result = int("".join(digits))

        return -result if is_negative else result