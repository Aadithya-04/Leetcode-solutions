from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = Counter(arr)
        occurrrences = list(freq.values())
        return len(occurrrences) == len(set(occurrrences))
# Time Complexity: O(n)
# Space Complexity: O(n)