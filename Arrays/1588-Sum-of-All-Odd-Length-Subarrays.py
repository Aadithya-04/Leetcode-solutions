class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total = 0
        n = len(arr)

        for i in range(n):
            end = i+1
            start = n-i
            total_subarray = end*start
            odd_count = (total_subarray+1)//2
            total += arr[i]*odd_count
        return total