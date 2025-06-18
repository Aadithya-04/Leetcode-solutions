class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        subsequence_sum = 0
        total_sum = sum(nums)
        subsequence = []

        for num in nums:
            subsequence_sum += num
            subsequence.append(num)
            if subsequence_sum > total_sum - subsequence_sum:
                break
        return subsequence
