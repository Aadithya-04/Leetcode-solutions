class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count_map = {0:-1}
        max_length = 0
        count = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                count -= 1
        
            if count in count_map:
                max_length = max(max_length,i-count_map[count])
            else:
                count_map[count] = i
        return max_length 