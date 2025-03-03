class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        totalSum = sum(arr)

        if totalSum % 3 != 0:
            return False
        
        target = totalSum//3

        partsFound = 0
        currentSum = 0

        for num in arr:
            currentSum += num 
            
            if currentSum == target:
                partsFound += 1
                currentSum = 0
        
        return partsFound >= 3
        