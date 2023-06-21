class Solution:
    def trailingZeroes(self, n: int) -> int:
        sys.set_int_max_str_digits(1999999999)
        print(n)
        ans = str(factorial(n))
        if (ans.count("0") == None):
            return 0 
        ans = ans[::-1]
        print(ans)
        answer = 0
        for i in ans:
            if (i == "0"):
                answer = answer + 1
            else:
                return answer
        return answer
    
    def factorial(n:int) -> int:
        if (n == 0):
            return 1
        return n * (factorial(n - 1))