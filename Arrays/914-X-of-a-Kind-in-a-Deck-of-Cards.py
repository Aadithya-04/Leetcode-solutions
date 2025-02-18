from collections import Counter
import math

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = Counter(deck)

        frequencies = list(count.values())
        gcdValue = frequencies[0]

        for freq in frequencies[1:]:
            gcdValue = math.gcd(gcdValue,freq)
            if gcdValue == 1:
                return False
        return gcdValue > 1   