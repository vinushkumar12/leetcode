class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        answer = []
        for i in nums:
            if i != val:
                answer.append(i)
        for x in range(len(answer)):
            nums[x] = answer[x]
        return len(answer)
        
        