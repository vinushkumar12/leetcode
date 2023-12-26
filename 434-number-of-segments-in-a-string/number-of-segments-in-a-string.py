class Solution:
    def countSegments(self, s: str) -> int:
        if s == "" or s.strip() == "":
            return 0
        answer = s.split(" ")
        counter = 0
        for i in answer:
            if i != "":
                counter = counter + 1
        return counter
        