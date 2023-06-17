class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        answer = arrivalTime + delayedTime
        if (answer < 24):
            return answer
        elif (answer == 24):
            return 0
        return answer % 24