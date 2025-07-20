class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        freq = {}

        result = []

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        for num in freq:
            if freq[num] == 1:
                result.append(num)
        return result
        