class Solution:
    def reverseString(self, lst: List[str]) -> None:
        index2 = 0       
        for index1 in range(len(lst) - 1, -1, -1):
            if (index2 == index1):
                break
            lst[index1], lst[index2] = lst[index2], lst[index1]
            index2 = index2+1
            if (index2 == index1):
                break
        return lst
            
