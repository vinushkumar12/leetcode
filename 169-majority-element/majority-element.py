class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        answer = {}
        if nums:
            for i in nums:
                if i in answer:
                    answer[i] += 1
                    if answer[i] > len(nums)/2:
                        return i
                else:
                    answer[i] = 1
            return nums[0]
        return
        
         