class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        distinct_candies = len(set(candyType))
        return min(distinct_candies,len(candyType)//2)