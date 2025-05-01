# Problem: Decimal to binary number using recursion - https://www.geeksforgeeks.org/decimal-binary-number-using-recursion/

class Solution:
    def decimalToBinary(self, n: int) -> int:
        if n == 0:
            return 0
            
        return n % 2 + 10 * self.decimalToBinary(n//2)