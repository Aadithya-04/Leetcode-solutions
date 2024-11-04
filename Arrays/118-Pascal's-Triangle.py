from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
    
        for row in range(numRows):
            # Start each row with 1
            current_row = [1] * (row + 1)
        
            # Each triangle element (except the first and last) is the sum of the two elements above it
            if row > 1:  # We can only do this for rows 2 and above
                for j in range(1, row):
                    current_row[j] = triangle[row - 1][j - 1] + triangle[row - 1][j]
        
            triangle.append(current_row)
    
        return triangle
        