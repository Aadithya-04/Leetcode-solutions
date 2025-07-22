class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        total = 0

        minLength = float('inf')

        for right in range(len(nums)):
            total += nums[right]    #add current number to the window sum
            while total >= target:
                minLength = min(minLength,right-left+1) #result updating 
                total -= nums[left]     #remove the leftmost element
                left += 1   #moving the window forward
        return 0 if minLength == float('inf') else minLength