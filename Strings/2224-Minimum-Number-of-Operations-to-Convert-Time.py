class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        # Split current and correct times into hours and minutes
        current_hours, current_minutes = map(int, current.split(':'))
        correct_hours, correct_minutes = map(int, correct.split(':'))

        # Convert both times to total minutes since 00:00
        current_total_minutes = current_hours * 60 + current_minutes
        correct_total_minutes = correct_hours * 60 + correct_minutes

        # Calculate the difference in minutes
        diff = correct_total_minutes - current_total_minutes
        operations = 0

        # Use a greedy approach to minimize the number of operations
        for op in [60, 15, 5, 1]:
            operations += diff // op  # How many times we can apply this operation
            diff %= op  # Reduce the difference by the number of minutes we've covered

        return operations
