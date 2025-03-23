class Solution:
    def checkString(self, s: str) -> bool:
        seen_b = False  # Flag to track if we have seen a 'b'
        
        for char in s:
            if char == 'b':
                seen_b = True  # Mark that we have seen a 'b'
            elif char == 'a' and seen_b:
                # If we see an 'a' after a 'b', return False
                return False
        
        return True
