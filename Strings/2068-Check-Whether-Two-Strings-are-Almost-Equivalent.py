from collections import Counter
class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        freq1 = Counter(word1)
        freq2 = Counter(word2)

        for char in range(26):
            letter = chr(char+ord('a'))
            diff = abs(freq1[letter]-freq2[letter])
            if diff > 3:
                return False
        
        return True

        