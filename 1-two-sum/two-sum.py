class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        access = {}
        for i in range(len(nums)):
            if target - nums[i] in access:
                return [i, access[target - nums[i]]]
            else:
                access[nums[i]] = i
        return

        