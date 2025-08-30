# Problem: Additive Number - https://leetcode.com/problems/additive-number/

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        def valid(num_str: str) -> bool:
            return not (len(num_str) > 1 and num_str[0] == '0')

        for i in range(1, n):
            for j in range(i+1, n):
                first, second = num[:i], num[i:j]
                if not valid(first) or not valid(second):
                    continue

                a, b = int(first), int(second)
                k = j
                while k < n:
                    c = a + b
                    c_str = str(c)
                    if not num.startswith(c_str, k):
                        break
                    k += len(c_str)
                    a, b = b, c
                if k == n:
                    return True
        return False