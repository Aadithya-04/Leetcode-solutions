from typing import List
class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        topView = 0
        topViewArea = 0

        for i in range(n):
            for j in range(n):
                if grid[i][j] > 0:
                    topViewArea += 1
        
        sideView_yz_Area = 0
        for j in range(n):
            sideView_yz_Area += max(grid[i][j] for i in range(n))

        sideView_zx_Area = 0
        for i in range(n):
            sideView_zx_Area += max(grid[i][j] for j in range(n))
        return topViewArea+sideView_yz_Area+sideView_zx_Area

        