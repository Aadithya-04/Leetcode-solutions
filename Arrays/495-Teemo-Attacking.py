class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        total_poison_time = 0
        poison_end = -1

        for time in timeSeries:
            if time >= poison_end:
                total_poison_time += duration
            else:
                total_poison_time += (time+duration-poison_end)
            poison_end = time + duration
        return total_poison_time
        