from collections import Counter 
class Solution:
    def frequencySort(self, s: str) -> str:
        frequency = Counter(s)
        return ''.join(char*frequency[char]for char in sorted(frequency,key=frequency.get,reverse=True))
        