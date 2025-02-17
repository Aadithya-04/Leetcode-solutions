class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        minVal = min(nums)
        maxVal = max(nums)

        return max(0,(maxVal-k)-(minVal+k))