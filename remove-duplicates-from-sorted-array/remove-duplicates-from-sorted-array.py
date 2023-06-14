class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp = list(set(nums))
        sort = sorted(temp[:len(temp)]) + temp[len(temp):]
        for i in range(len(sort)):
            nums[i] = sort[i]
        print(nums)
        return len(temp)
        