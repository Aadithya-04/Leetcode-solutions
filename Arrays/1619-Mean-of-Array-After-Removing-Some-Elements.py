class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        n = len(arr)
        cut = n//20
        trimmedArray = arr[cut:n-cut]
        return sum(trimmedArray)/len(trimmedArray)