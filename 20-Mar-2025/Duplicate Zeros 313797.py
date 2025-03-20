# Problem: Duplicate Zeros - https://leetcode.com/problems/duplicate-zeros/description/?envType=problem-list-v2&envId=two-pointers

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        arr_new = []
        size = len(arr)
        for num in arr:
            if num == 0:
                arr_new.append(num)
                arr_new.append(num)
            else:
                arr_new.append(num)
        print(arr_new)
        arr.clear()
        for i in range(size):
            arr.append(arr_new[i])
        