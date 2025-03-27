class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        col1, row1, col2, row2 = s[0], s[1], s[3], s[4]
    
    # Convert column letters to their respective indices (A=1, B=2, ..., Z=26)
        start_col = ord(col1) - ord('A') + 1
        end_col = ord(col2) - ord('A') + 1
    
    # Convert rows from string to integer
        start_row = int(row1)
        end_row = int(row2)
    
    # List to store the result
        result = []
    
    # Loop through columns from start_col to end_col
        for col in range(start_col, end_col + 1):
        # Loop through rows from start_row to end_row
            for row in range(start_row, end_row + 1):
            # Convert column index back to letter
                col_letter = chr(ord('A') + col - 1)
            # Append the cell in the required format
                result.append(f"{col_letter}{row}")
    
        return result