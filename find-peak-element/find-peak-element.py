class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range (len(nums)):
            if (i + 1 < len(nums) and nums[i] > nums[i + 1]):
                if (i != 0 and nums[i - 1] < nums[i]):
                    return i
                else:
                    return i
            elif (i + 1 == len(nums)):
                if (nums[i - 1] < nums[i]):
                    return i
        return 0