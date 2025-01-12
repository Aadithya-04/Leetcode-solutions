class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morseCode = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        morseMap = {chr(i+ord('a')):morseCode[i] for i in range(26)}
        transformations = set()
        for word in words:
            transformation = ''.join(morseMap[char] for char in word)
            transformations.add(transformation)
        return len(transformations)