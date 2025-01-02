class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for num in nums:
            index = abs(num)-1
            if nums[index] > 0:
                nums[index] = -nums[index]

        missing_number = []

        for i in range(n):
            if nums[i] > 0:
                missing_number.append(i+1)
        return missing_number 
        