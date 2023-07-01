class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ans = {}
        for i in nums:
            if i in ans:
                ans[i] += 1
            else:
                ans[i] = 1
        temp = set()
        for x in ans:
            if (ans[x] == 1 and x not in temp):
                temp.add(x)
        return list(temp)