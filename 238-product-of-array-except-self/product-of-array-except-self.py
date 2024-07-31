class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = [1] * len(nums)
        prefix = 1
        postfix = 1
        for i in range(len(nums)):
            if i == 0:
                arr[0] = 1
            else:
                arr[i] *= prefix
            prefix *= nums[i]
        print(arr)
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                arr[len(nums) - 1] *= 1
            else:
                arr[i] *= postfix
            postfix *= nums[i]
        return arr

            


        