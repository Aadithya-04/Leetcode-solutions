class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = set('aeiou')
        n = len(word)
        count = 0

        for i in range(n):
            if word[i] in vowels:
                vowelCount = set()
                for j in range(i,n):
                    if word[j] in vowels:
                        vowelCount.add(word[j])
                        if len(vowelCount) == 5:
                            count+=1
                    else:
                        break
        return count