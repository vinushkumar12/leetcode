class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        ans = []
        for i in counter:
            if (counter[i] > len(nums)/3):
                ans.append(i)
        return ans
