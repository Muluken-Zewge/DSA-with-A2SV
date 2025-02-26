# Problem: Rearrange Array Elements by Sign - https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pstv_nums,ngtv_nums = [], []
        
        for num in nums:
            if num > 0:
                pstv_nums.append(num)
            else:
                ngtv_nums.append(num)

        answer = []
        pstv_pointer = 0
        ngtv_pointer = 0

        for i in range(len(nums)):
            if i % 2 == 0:
                answer.append(pstv_nums[pstv_pointer])
                pstv_pointer += 1
            else:
                answer.append(ngtv_nums[ngtv_pointer])
                ngtv_pointer += 1
        
        return answer