from typing import List
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        inDegree = [0]*(n+1)
        outDegree = [0]*(n+1)

        for i,j in trust:
            outDegree[i]+=1
            inDegree[j]+=1

        for i in range(1,n+1):
            if outDegree[i] == 0 and inDegree[i] == n-1:
                return i
        return -1
        