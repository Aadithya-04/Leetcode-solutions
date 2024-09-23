class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = current_sum = sum(nums[:k])
    
    # Step 2: Slide the window through the rest of the array
        for i in range(k, len(nums)):
        # Update the current sum by sliding the window
            current_sum += nums[i] - nums[i - k]
        
        # Update max_sum if the current_sum is greater
            max_sum = max(max_sum, current_sum)
    
    # Step 3: Calculate the maximum average
        return max_sum / k
        