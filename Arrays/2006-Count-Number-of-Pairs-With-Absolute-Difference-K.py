from collections import defaultdict
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        count = 0

        for num in nums:
            if num+k in freq:
                count += freq[num+k]
            if num-k in freq:
                count += freq[num-k]

            freq[num]+=1
        return count
        
