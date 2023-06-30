class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def perm(temp):
            if (len(temp) == 1):
                return [temp]
            all_perm = []
            for x in range(len(temp)):
                curr = temp[x]
                remaining = temp[:x] + temp[x + 1:]
                for i in perm(remaining):
                    t = [curr] + i
                    if t not in all_perm:
                        all_perm.append([curr] + i)
            return all_perm
        return perm(nums) 