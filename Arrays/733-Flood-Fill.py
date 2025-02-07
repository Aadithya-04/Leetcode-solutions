from typing import List
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]
        if original_color == color:
            return image
        
        def dfs(r,c):
            if r<0 or r>=len(image) or c < 0 or c>=len(image[0]) or image[r][c] != original_color:
                return
            
            image[r][c] = color 

            dfs(r - 1, c)  # Up
            dfs(r + 1, c)  # Down
            dfs(r, c - 1)  # Left
            dfs(r, c + 1)  # Right

        dfs(sr,sc)
        return image 