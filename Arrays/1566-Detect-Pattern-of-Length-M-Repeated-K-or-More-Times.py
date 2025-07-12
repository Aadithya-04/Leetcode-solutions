class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        n = len(arr)
        for i in range(n-m*k+1):
            pattern =  arr[i:i+m]
            count = 1
            for j in range(i+m,i+m*k):
                if arr[j:j+m] == pattern:
                    count+=1
                else:
                    break
            if count >= k:
                return True
        return False
        