class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        strengths = []
        for i in range(len(mat)):
            soldier_count = sum(mat[i])
            strengths.append((soldier_count,i))
        strengths.sort()

        return [index for _,index in strengths[:k]]



