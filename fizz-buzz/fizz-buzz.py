class Solution(object):
    def fizzBuzz(self, n):
        answer = []
        for i in range(1, n + 1):
            divisible_3 = i % 3 == 0
            divisible_5 = i % 5 == 0
            if (divisible_3 and divisible_5):
                answer.append("FizzBuzz")
            elif (divisible_5):
                answer.append("Buzz")
            elif (divisible_3):
                answer.append("Fizz")
            else:
                answer.append(str(i))
        return answer