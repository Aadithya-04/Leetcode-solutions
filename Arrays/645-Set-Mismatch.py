class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sum_ideal = n*(n+1)//2
        sum_square_ideal = n*(2*n+1)*(n+1)//6

        sum_nums = sum(nums)
        sum_squares = sum(x*x for x in nums)

        diff_sum = sum_nums-sum_ideal
        diff_squares = sum_squares-sum_square_ideal

        sum_dupl_missing = diff_squares//diff_sum

        duplicate = (diff_sum+sum_dupl_missing)//2
        missing = duplicate - diff_sum

        return [duplicate,missing]