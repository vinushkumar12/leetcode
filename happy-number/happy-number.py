class Solution:
    def isHappy(self, n: int) -> bool:
        num = str(n)
        sets = set()
        while (num not in sets):
            sets.add(num)
            temp = 0
            for i in num:
                temp += int(i) ** 2
            if (temp == 1):
                return True
            num = str(temp)
        return False


