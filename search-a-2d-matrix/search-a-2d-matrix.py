class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            start = 0
            end = len(i) - 1
            if i[len(i) - 1] >= target and i[0] <= target:
                while (start <= end):
                    middle = (end + start) // 2
                    if (i[middle] == target):
                        return True
                    elif (i[middle] > target):
                        end = middle - 1
                    elif (i[middle] < target):
                        start = middle + 1
        return False

                
