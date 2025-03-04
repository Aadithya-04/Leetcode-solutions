from typing import List 
class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        result = []
        num = 0

        for bit in nums:
            num = (num*2+bit)%5
            result.append(num==0)
        return result 
        