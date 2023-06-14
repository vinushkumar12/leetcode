class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums)
        frequency = sorted(frequency.items(), key=lambda x: x[1], reverse = True)
        print(frequency)
        answer = []
        i = 0
        while i < k:
            answer.append(frequency[i][0])
            i += 1
        return answer
            