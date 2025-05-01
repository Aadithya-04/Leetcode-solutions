class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        n = len(arr)
        i = 0
        j = 0

        while j < n:
            if arr[i] == 0:
                if j == n - 1:
                    arr[-1] = 0
                    n -= 1
                    break
                j += 1
            i += 1
            j += 1

        i -= 1
        j -= 1

        while i >= 0:
            if j < len(arr):
                arr[j] = arr[i]
            if arr[i] == 0:
                j -= 1
                if j < len(arr):
                    arr[j] = 0
            i -= 1
            j -= 1
