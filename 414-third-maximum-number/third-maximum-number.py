class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        larger = [int(-sys.maxsize - 1),int(-sys.maxsize - 1),int(-sys.maxsize - 1)]
        for i in range(len(nums)):
            print(larger)
            if nums[i] > larger[0]:
                larger[2] = larger[1]
                larger[1] = larger[0]
                larger[0] = nums[i]
            elif nums[i] > larger[1] and nums[i] != larger[0]:
                larger[2] = larger[1]
                larger[1] = nums[i]
            elif nums[i] > larger[2] and nums[i] != larger[0] and nums[i] != larger[1]:
                larger[2] = nums[i]
        print(larger)
        if len(nums) < 3 or larger[2] == int(-sys.maxsize - 1):
            return larger[0]
        return larger[2]
                