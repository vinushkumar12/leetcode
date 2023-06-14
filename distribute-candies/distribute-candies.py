class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        unique = set(candyType)
        if (len(candyType)/2 > len(unique)):
            return len(unique)
        elif (len(candyType)/2 < len(unique)):
            return int(len(candyType)/2)
        return len(unique)