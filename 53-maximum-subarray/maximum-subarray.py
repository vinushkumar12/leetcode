class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        high_sum = nums[0]
        curr_sum = 0
        for i in nums:
            curr_sum += i
            if curr_sum > high_sum:
                high_sum = curr_sum
            if curr_sum < 0:  
                curr_sum = 0
        return high_sum
        
            

        