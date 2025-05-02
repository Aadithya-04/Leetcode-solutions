class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        result = 0

        for num in nums:
            countDigits = 0
            while num != 0:
                num //=10
                countDigits += 1
            if countDigits % 2 == 0:
                result += 1
        return result