from typing import List

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows = len(img)
        cols = len(img[0])
        
        result = [[0] * cols for _ in range(rows)]
        
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), 
                      (-1, -1), (-1, 1), (1, -1), (1, 1)]
        
        for i in range(rows):
            for j in range(cols):
                sum_pixels = img[i][j]
                count = 1  
                
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < rows and 0 <= nj < cols:
                        sum_pixels += img[ni][nj]
                        count += 1
                
                result[i][j] = sum_pixels // count
        
        return result
