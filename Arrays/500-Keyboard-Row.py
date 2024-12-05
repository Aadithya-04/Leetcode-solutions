class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        
        # Prepare an empty list to store the result
        result = []
        
        # Iterate through each word in the input list
        for word in words:
            # Convert word to lowercase for checking, but keep original word for output
            lower_word = word.lower()
            
            # Check which row the first character belongs to
            if all(char in row1 for char in lower_word):
                result.append(word)
            elif all(char in row2 for char in lower_word):
                result.append(word)
            elif all(char in row3 for char in lower_word):
                result.append(word)
        
        return result
        