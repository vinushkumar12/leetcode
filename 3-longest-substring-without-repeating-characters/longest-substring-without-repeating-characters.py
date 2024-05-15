class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        leng = 0
        answer = set()
        for i in range(len(s)):
            answer.add(s[i])
            for x in range(i + 1, len(s)):
                if s[x] in answer:
                    if leng < len(answer):
                        leng = len(answer)
                    answer = set()
                    break
                else:
                    answer.add(s[x])
        return max(leng, len(answer))