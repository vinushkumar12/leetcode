class Solution: 
    def maximumGap(self, nums: List[int]) -> int:
        sorted_arr = sorted(nums)
        maximum = 0
        for i in range(len(sorted_arr) - 1):
            maximum = max(maximum, sorted_arr[i+1] - sorted_arr[i])
        return maximum

        