class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result, current_line, current_length = [], [], 0

        for word in words:
            if current_length + len(word) + len(current_line) > maxWidth:
                spaces_to_add = maxWidth - current_length
                if len(current_line) == 1:
                    result.append(current_line[0] + ' ' * spaces_to_add)
                else:
                    space_between_words = spaces_to_add // (len(current_line) - 1)
                    extra_spaces = spaces_to_add % (len(current_line) - 1)
                    for i in range(extra_spaces):
                        current_line[i] += ' '
                    result.append((' ' * space_between_words).join(current_line))
                current_line, current_length = [], 0
            
            current_line.append(word)
            current_length += len(word)
        
        result.append(' '.join(current_line).ljust(maxWidth))
        return result
