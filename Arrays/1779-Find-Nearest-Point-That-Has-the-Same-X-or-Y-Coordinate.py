class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_distance = float('inf')
        nearest_index = -1

        for i,(xi,yi) in enumerate(points):
            if xi == x or yi == y:
                dist = abs(x-xi) + abs(y-yi)
                if dist < min_distance:
                    min_distance = dist
                    nearest_index = i
        return nearest_index