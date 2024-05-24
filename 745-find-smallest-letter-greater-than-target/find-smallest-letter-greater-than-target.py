class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        difference = inf
        lower = 0
        higher = len(letters) - 1
        while lower <= higher:
            middle = (higher + lower) // 2
            if (letters[middle] == target):
                while letters[middle] <= target:
                    middle = middle + 1
                    if middle == len(letters):
                        return letters[0]
                return letters[middle]
            elif (letters[middle] > target):
                higher = middle - 1
                if (ord(letters[middle]) - ord(target) < difference):
                    difference = ord(letters[middle]) - 97
                else:
                    break
            elif (ord(letters[middle]) < ord(target)):
                lower = middle + 1
        if difference == inf:
            return letters[0]
        return chr(difference + 97)
        