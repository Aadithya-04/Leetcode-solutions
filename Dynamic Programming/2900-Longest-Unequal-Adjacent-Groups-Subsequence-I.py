class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)

        dp = [1]*n
        prev = [-1]*n

        for i in range(n):
            for j in range(i):
                if groups[i] != groups[j]:
                    if dp[i] < dp[j]+1:
                        dp[i] = dp[j] + 1
                        prev[i] = j
        max_length = max(dp)
        index = dp.index(max_length)

        subsequence = []
        while index!=-1:
            subsequence.append(words[index])
            index = prev[index]
        subsequence.reverse()

        return subsequence