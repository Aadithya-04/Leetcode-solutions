class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1 
        elif n == 2:
            return 2

        prev2 , prev1 = 1,2

        for i in range(3,n+1):
            current = prev2 + prev1
            prev2 = prev1
            prev1 = current
        return prev1
        