class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        return count.most_common()[0][0]
        