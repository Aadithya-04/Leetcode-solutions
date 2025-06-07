class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        if not grid or not grid[0]:
            return grid

        m, n = len(grid), len(grid[0])
        total = m * n
        k %= total  # optimize for large k

        # Flatten the grid into a 1D list
        flat = [grid[i][j] for i in range(m) for j in range(n)]

        # Shift the list
        shifted = flat[-k:] + flat[:-k]

        # Convert back to 2D grid
        result = [[shifted[i * n + j] for j in range(n)] for i in range(m)]

        return result
# Time Complexity: O(m * n)
# Space Complexity: O(m * n)
