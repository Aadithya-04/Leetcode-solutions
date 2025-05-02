class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = 0
        i = 0
        while i < len(nums):
            nums[i] = nums[i] + res
            res = nums[i]
            i+=1
        return nums
