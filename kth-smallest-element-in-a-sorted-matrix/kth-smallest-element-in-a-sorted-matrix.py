import numpy as np
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        answer = []
        for i in matrix:
            answer += i
        return sorted(answer)[k-1]