class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        numInt = 0
        for digit in num:
            numInt = numInt * 10 + digit

        total = numInt + k
        
        # Construct the result from the total using modulus and integer division
        result = []
        while total > 0:
            result.append(total % 10)
            total //= 10
        
        # Reverse the list since we append digits in reverse order
        return result[::-1]
