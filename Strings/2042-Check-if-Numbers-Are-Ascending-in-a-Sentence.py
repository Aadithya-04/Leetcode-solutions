class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        tokens = s.split()
        lastNumber = -1

        for token in tokens:
            if token.isdigit():
                num = int(token)
                if num<=lastNumber:
                    return False
                lastNumber = num
        return True
        