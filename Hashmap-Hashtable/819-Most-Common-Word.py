import re
from collections import Counter 
from typing import List

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # Normalize the paragraph: convert to lowercase and remove punctuation
        paragraph = re.sub(r'[^\w\s]', ' ', paragraph).lower()
        
        # Split the paragraph into words
        words = paragraph.split()
        
        # Create a Counter to count the frequency of each word
        word_count = Counter(words)
        
        # Convert banned list to a set for faster lookups
        banned_set = set(banned)
        
        # Initialize variables to track the most frequent non-banned word
        most_common_word = ""
        max_count = 0
        
        # Find the most common word that is not banned
        for word, count in word_count.items():
            if word not in banned_set and count > max_count:
                most_common_word = word
                max_count = count
        
        return most_common_word


