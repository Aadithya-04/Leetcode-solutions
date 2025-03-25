class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        result = []
        for i in range(0, len(s), k):
            group = s[i:i+k]  # Get the substring from i to i+k
            if len(group) < k:
            # If the group is shorter than k, fill it up
                group += fill * (k - len(group))
            result.append(group)
    
        return result