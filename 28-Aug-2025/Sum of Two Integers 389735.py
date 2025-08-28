# Problem: Sum of Two Integers - https://leetcode.com/problems/sum-of-two-integers/description/

class Solution:
    def getSum(self, a: int, b: int) -> int:
    # 32-bit mask (to handle negative numbers in Python since it has infinite int size)
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF

        while b != 0:
            # XOR for sum without carry
            s = (a ^ b) & mask
            # AND+shift for carry
            carry = ((a & b) << 1) & mask

            a, b = s, carry

        # If a is within signed 32-bit range, return as is
        return a if a <= max_int else ~(a ^ mask)
