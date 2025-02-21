class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        # Check minimum length
        if len(arr) < 3:
            return False
            
        # Find peak index
        peak = 0
        for i in range(1, len(arr)):
            if arr[i] <= arr[i-1]:
                peak = i - 1
                break
        else:  # This triggers if loop completes without breaking
            return False
            
        # Peak can't be at start
        if peak == 0:
            return False
            
        # Check strictly decreasing after peak
        for i in range(peak + 1, len(arr)):
            if arr[i] >= arr[i-1]:
                return False
                
        return True