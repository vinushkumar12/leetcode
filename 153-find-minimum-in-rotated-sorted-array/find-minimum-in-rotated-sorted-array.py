class Solution:
    def findMin(self, nums: List[int]) -> int:
        mini = nums[0]
        l,r = 0, len(nums) - 1
        while l <= r:
            print("l", l)
            print("r", r)
            if nums[l] <= nums[r]:
                return min(nums[l], mini)
            middle = (l + r) // 2
            mini = min(nums[middle], mini)
            if nums[middle] >= nums[l]:
                l = middle + 1
            else:
                r = middle - 1
        return mini

