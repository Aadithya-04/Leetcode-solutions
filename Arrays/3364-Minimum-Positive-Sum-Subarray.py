class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        prefix = [0]*(n+1)

        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]
        
        minSum = float('inf')

        for size in range(l,r+1):
            for i in range(size,n+1):
                total = prefix[i] - prefix[i-size]
                if total > 0:
                    minSum = min(minSum,total)
        return minSum if minSum != float('inf') else -1
