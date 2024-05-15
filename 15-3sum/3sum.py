class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if nums is None:
            return None
        nums.sort()
        res = []
        for i in range(len(nums)):
            if (i > 0 and nums[i - 1] != nums[i]) or i == 0:
                j = i + 1
                k = len(nums) - 1
                while j < k:
                    if (nums[i] + nums[k] + nums[j] == 0):
                        res.append([nums[i], nums[j], nums[k]])
                        j += 1
                        while (nums[j] == nums[j - 1] and j < k):
                            j = j + 1
                    elif (nums[i] + nums[k] + nums[j] > 0):
                        k = k - 1
                    elif (nums[i] + nums[k] + nums[j] < 0):
                        j = j + 1
        return res
                    


        
        
        