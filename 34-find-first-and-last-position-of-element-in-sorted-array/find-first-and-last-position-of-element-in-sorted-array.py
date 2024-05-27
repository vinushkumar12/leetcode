class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        solution = [-1,-1]
        lower = 0
        higher = len(nums) - 1
        while lower <= higher:
            middle = (lower + higher) // 2
            if nums[middle] == target:
                counter = 1
                solution[0] = middle
                solution[1] = middle
                while middle + counter < len(nums) and nums[middle + counter] == target:
                    solution[1] = middle + counter
                    counter += 1
                counter = 1
                while middle - counter >= 0 and nums[middle - counter] == target:
                    solution[0] = middle - counter
                    counter += 1
                return solution
            elif nums[middle] > target:
                higher = middle - 1
            elif nums[middle] < target:
                lower = middle + 1
        return solution