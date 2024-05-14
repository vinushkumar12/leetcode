class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = 0
        sum_max = -inf
        for i in nums:
            if (i + current_sum > i):
                current_sum = i + current_sum
            else:
                current_sum = i
            if (current_sum > sum_max):
                sum_max = current_sum
        return sum_max
            

        