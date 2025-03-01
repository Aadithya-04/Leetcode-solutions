from collections import Counter 
from typing import List 

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        commonCount = Counter(words[0])

        for word in words[1:]:
            wordCount = Counter(word)
            commonCount &= wordCount

        result = []
        for char,count in commonCount.items():
            result.extend([char]*count)

        return result