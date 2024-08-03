class Solution:
    def findMin(self, nums: List[int]) -> int:
        index = len(nums) // 2
        minimum = nums[0]
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            if nums[0] > nums[1]:
                return nums[1]
            return nums[0]
        if nums[index + 1] < nums[index]:
            return nums[index + 1]
        elif nums[index + 1] > nums[index]:
            for i in range(0, index + 1):
                if nums[i] < minimum:
                    minimum = nums[i]
            for i in range(index + 1, len(nums)):
                if nums[i] < minimum:
                    minimum = nums[i]
        return minimum
