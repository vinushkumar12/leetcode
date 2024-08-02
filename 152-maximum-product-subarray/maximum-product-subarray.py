class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product, min_product = 1,1
        maxi = max(nums)
        for i in nums:
            if i == 0:
                max_product = 1
                min_product = 1
            else:
                temp = max_product
                max_product = max(i * max_product, i, i * min_product)
                min_product = min(i * temp, i , i * min_product)
                maxi = max(max_product, maxi)
        return maxi
            
        