class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        surface_area = 0

        for i in range(n):
            for j in range(n):
                if grid[i][j] > 0:
                    # Each cube contributes 6 faces
                    surface_area += grid[i][j] * 6
                    
                    # Subtract the faces that are hidden within the same stack
                    if grid[i][j] > 1:
                        # For a stack of height h, h-1 faces are hidden inside
                        surface_area -= (grid[i][j] - 1) * 2
                    
                    # Subtract faces that are adjacent to neighboring stacks
                    if i > 0:  # Neighbor above
                        surface_area -= min(grid[i][j], grid[i-1][j]) * 2
                    if j > 0:  # Neighbor to the left
                        surface_area -= min(grid[i][j], grid[i][j-1]) * 2

        return surface_area