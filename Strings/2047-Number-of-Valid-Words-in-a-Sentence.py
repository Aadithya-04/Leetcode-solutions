import re

class Solution:
    def countValidWords(self, sentence: str) -> int:
        words = sentence.split()
        validWordCount = 0
        
        # Updated regex to allow a single punctuation mark or a valid word with letters and punctuation
        validWordPattern = re.compile(r'^[a-z]+(-[a-z]+)?[!.,]?$|^[!.,]$')

        for word in words:
            if validWordPattern.match(word):
                validWordCount += 1

        return validWordCount
