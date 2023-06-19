class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        print(strs)
        counter_1 = 0
        counter_2 = 0
        answer = ""
        while (counter_1 < len(strs[0]) and counter_2 < len(strs[-1])):
            if (strs[0][counter_1] != strs[-1][counter_2]):
                return answer
            answer = answer + strs[0][counter_1]
            counter_1 = counter_1 + 1
            counter_2 = counter_2 + 1
        return answer
