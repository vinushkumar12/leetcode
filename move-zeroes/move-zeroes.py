class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        c = nums.count(0)
        for i in range(c):
            nums.remove(0)
        nums.extend([0] * c)
        return nums