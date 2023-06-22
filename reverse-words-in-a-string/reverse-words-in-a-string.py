class Solution:
    def reverseWords(self, s: str) -> str:
        split_list = s.split()
        split_list = split_list[::-1]
        ans = ""
        for i in range(len(split_list)):
            if i == 0:
                ans = split_list[i]
            else:
                ans = ans + " " + split_list[i]
        return ans
