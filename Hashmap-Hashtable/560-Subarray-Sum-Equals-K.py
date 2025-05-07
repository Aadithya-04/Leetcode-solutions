class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash_sum_count = {0:1}
        current_sum = 0
        count = 0

        for num in nums:
            current_sum += num 
            if (current_sum-k) in hash_sum_count:
                count += hash_sum_count[current_sum-k]
            hash_sum_count[current_sum] = hash_sum_count.get(current_sum,0)+1
        return count 