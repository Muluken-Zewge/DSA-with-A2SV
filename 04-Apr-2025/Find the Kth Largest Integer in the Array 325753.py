# Problem: Find the Kth Largest Integer in the Array - https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums_num = list(map(int, nums))# create list of integers from nums
        nums_num.sort(reverse=True)

        return str(nums_num[k-1])