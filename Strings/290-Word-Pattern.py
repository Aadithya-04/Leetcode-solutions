class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        # If the number of words does not match the number of characters in the pattern
        if len(pattern) != len(words):
            return False
        
        # Dictionaries to map pattern -> word and word -> pattern
        pattern_to_word = {}
        word_to_pattern = {}

        # Iterate through the pattern and words simultaneously
        for p, w in zip(pattern, words):
            # Check if the pattern is already mapped to a different word
            if p in pattern_to_word:
                if pattern_to_word[p] != w:
                    return False
            else:
                pattern_to_word[p] = w

            # Check if the word is already mapped to a different pattern
            if w in word_to_pattern:
                if word_to_pattern[w] != p:
                    return False
            else:
                word_to_pattern[w] = p
        
        return True
