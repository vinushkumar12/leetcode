class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        counter = nums.count(target)
        if (counter == 0):
            return [-1, -1]
        index = nums.index(target)
        if (counter == 1):
            return [index, index]
        return [index, index + counter - 1]