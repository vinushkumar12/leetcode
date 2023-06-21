class Solution:
    def reverseBits(self, n: int) -> int:
        temp = bin(n)[2:].zfill(32)
        temp = temp[::-1]
        return int(temp, 2)
       
        
        
        