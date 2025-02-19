class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even, odd = 0, 1  # Start with even at index 0 and odd at index 1
        
        while even < len(nums) and odd < len(nums):
            if nums[even] % 2 == 0:
                even += 2  # Move even pointer to the next even index
            elif nums[odd] % 2 != 0:
                odd += 2  # Move odd pointer to the next odd index
            else:
                # Swap if even is odd and odd is even
                nums[even], nums[odd] = nums[odd], nums[even]
                even += 2  # Move even pointer
                odd += 2   # Move odd pointer
        
        return nums
