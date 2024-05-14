class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = 0
        top_sum = -inf
        for i in nums:
            if curr_sum + i > i:
                curr_sum = curr_sum + i
            else:
                curr_sum = i
            if curr_sum > top_sum:
                top_sum = curr_sum
        return top_sum

        