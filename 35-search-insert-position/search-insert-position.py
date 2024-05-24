class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        possible = 0
        higher = len(nums) - 1
        lower = 0
        while lower <= higher:
            middle = (higher + lower) // 2
            if (nums[middle] == target):
                return middle
            elif (nums[middle] > target):
                if (nums[middle - 1] < target):
                    possible = middle
                else:
                    possible = middle - 1
                    if possible < 0:
                        possible = 0
                higher = middle - 1
            elif (nums[middle] < target):
                possible = middle + 1
                lower = middle + 1
        return possible