class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num_str = ''.join(str(ord(c)-ord('a')+1)for c in s)

        current_value = int(num_str)

        for _ in range(k):
            current_value = sum(int(digit)for digit in str(current_value))
        return current_value
        