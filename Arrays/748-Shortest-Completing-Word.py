from collections import Counter 
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        licensePlate = ''.join(filter(str.isalpha, licensePlate)).lower()
        license_count = Counter(licensePlate)

        shortest_word = None

        for word in words:
            word_count = Counter(word)
            # Check if word has all required characters with the correct frequencies
            if all(word_count[char] >= license_count[char] for char in license_count):
                if shortest_word is None or len(word) < len(shortest_word):
                    shortest_word = word
        
        return shortest_word