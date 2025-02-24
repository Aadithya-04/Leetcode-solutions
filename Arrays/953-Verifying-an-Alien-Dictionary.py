class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # Step 1: Create a dictionary to map each letter to its index in the alien alphabet
        order_map = {char: i for i, char in enumerate(order)}
        
        # Step 2: Compare each word with the next one in the list
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            
            # Compare the two words character by character
            min_length = min(len(word1), len(word2))
            for j in range(min_length):
                if order_map[word1[j]] < order_map[word2[j]]:
                    break
                elif order_map[word1[j]] > order_map[word2[j]]:
                    return False
            
            # If word1 is a prefix of word2 but longer, return False
            if len(word1) > len(word2) and word1[:min_length] == word2[:min_length]:
                return False
        
        return True
