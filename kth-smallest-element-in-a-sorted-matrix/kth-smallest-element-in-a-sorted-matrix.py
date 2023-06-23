import numpy as np
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        array = np.array(matrix).flatten()
        array.sort()
        return array[k - 1]