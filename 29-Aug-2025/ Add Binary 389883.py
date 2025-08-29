# Problem:  Add Binary - https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_num = int(a,2)
        b_num = int(b,2)
        sum = a_num + b_num

        return bin(sum)[2:]