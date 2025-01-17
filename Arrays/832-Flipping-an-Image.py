class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for rows in image:
            rows[:] = [1-pixel for pixel in reversed(rows)]
        return image