class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        lower = 0
        higher = len(letters) - 1
    
    # If the target is greater than or equal to the last element, wrap around to the first element
        if target >= letters[-1]:
            return letters[0]
    
        while lower <= higher:
            middle = (higher + lower) // 2
            if letters[middle] > target:
                higher = middle - 1
            else:
                lower = middle + 1
    
        return letters[lower]
        