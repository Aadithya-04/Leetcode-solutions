from collections import defaultdict
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        frequency = defaultdict(int)
        first_occurence = {}
        last_occurence = {}

        for i,num in enumerate(nums):
            frequency[num]+=1
            if num not in first_occurence:
                first_occurence[num] = i
            last_occurence[num] = i

        degree = max(frequency.values())

        shortest_length = float('inf')
        for num in frequency:
            if frequency[num] == degree:
                subarray_length = last_occurence[num]-first_occurence[num]+1
                shortest_length = min(shortest_length,subarray_length)

        return shortest_length
