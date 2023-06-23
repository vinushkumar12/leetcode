class Solution:
    def sortColors(self, nums: List[int]) -> None:
        def quicksort(nums):
            if len(nums) <= 1:
                return nums
            else:
                pivot = nums[0]
                less = [x for x in nums[1:] if x <= pivot]
                greater = [x for x in nums[1:] if x > pivot]
                return quicksort(less) + [pivot] + quicksort(greater)     
        modified = quicksort(nums)
        for i in range(len(modified)):
            nums[i] = modified[i]
        return nums
        