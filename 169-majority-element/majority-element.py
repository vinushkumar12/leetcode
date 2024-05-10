class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        answer = 0
        count = 0
        if nums:
            for i in nums:
                if count == 0:
                    answer = i
                if answer == i:
                    count = count + 1
                elif answer != i:
                    count = count - 1
        return answer
        
         