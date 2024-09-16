class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEatAll(speed):
            time = 0
            for pile in piles:
                time += (pile+speed-1)//speed
            return time <= h

        left,right = 1,max(piles)

        while left < right:
            mid = (left+right)//2
            if canEatAll(mid):
                right = mid
            else:
                left = mid+1

        return left
        