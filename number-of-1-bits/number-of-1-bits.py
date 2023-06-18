class Solution:
    def hammingWeight(self, n: int) -> int:
        n = bin(n)
        print(n)
        return n.count("1")