from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        
       
        dp = points[0]
        
        
        for r in range(1, m):
            
            max_left = [0] * n
            max_right = [0] * n
            max_left[0] = dp[0] + 0  
            max_right[n-1] = dp[n-1] - (n-1) 
            
            for c in range(1, n):
                max_left[c] = max(max_left[c-1], dp[c] + c)
                
            for c in range(n-2, -1, -1):
                max_right[c] = max(max_right[c+1], dp[c] - c)
            
        
            new_dp = [0] * n
            for c in range(n):
                new_dp[c] = points[r][c] + max(max_left[c] - c, max_right[c] + c)
            
            dp = new_dp
        
        
        return max(dp)
