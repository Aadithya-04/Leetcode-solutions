from collections import Counter 
from typing import List
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = Counter(arr)
        distinctStrings = [s for s in arr if count[s]==1]
        return distinctStrings[k-1] if k <= len(distinctStrings)else""