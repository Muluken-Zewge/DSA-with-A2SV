# Problem: K-th Symbol in Grammar - https://leetcode.com/problems/k-th-symbol-in-grammar/description/

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:

        if n == 1:
            return 0
        prevRow = self.kthGrammar(n-1,(k+1)//2)

        if k % 2 == 1:
            return prevRow
        else:
            return 1 - prevRow
        
        # def helper(row,n):
        #     if n == 1:
        #         return row[k-1]
        #     nextRow = []
        #     for char in row:
        #         if char == '0':
        #             nextRow.append('01')
        #         else:
        #             nextRow.append('10')
            
        #     nextRow = ''.join(nextRow)
        #     print('row',len(row))
        #     print('nextRow',len(nextRow))
        #     return helper(nextRow, n-1)
            
        # return int(helper('0',n))