class Solution:
    def minTimeToType(self, word: str) -> int:
        time = 0
        current_position = 0

        for char in word:
            target_position = ord(char) - ord('a')
            clockwise_direction = (target_position-current_position)%26
            counterclockwise_direction = (current_position-target_position)%26

            time += min(clockwise_direction,counterclockwise_direction)+1
            current_position = target_position
        return time