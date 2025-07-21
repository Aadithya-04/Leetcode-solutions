class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        uniqueSet = set(sentence)
        return len(uniqueSet) == 26