from collections import Counter
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count = Counter(s)
        frequencies = list(count.values())
        return len(set(frequencies)) == 1
        
        