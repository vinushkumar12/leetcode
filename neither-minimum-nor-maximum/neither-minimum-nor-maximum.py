class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        filtered_numbers = list(filter(lambda x: x != max(nums) and x != min(nums), nums))
        if (len(filtered_numbers) != 0):
            return filtered_numbers[0]
        return -1