class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines = 1
        currentWidth = 0

        for char in s:
            charWidth = widths[ord(char)-ord('a')] #getting the width of the character
            if currentWidth + charWidth > 100:
                lines += 1
                currentWidth = charWidth
            else:
                currentWidth += charWidth
        return [lines, currentWidth]      