class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        # Initialize the result to an empty string
        result = ""
        
        # Iterate through the string number
        for i in range(len(number) - 1):
            # If the current digit is equal to the target digit, check the next digit
            if number[i] == digit:
                # If the next digit is larger than the current one, remove the current one
                if number[i + 1] > number[i]:
                    return number[:i] + number[i + 1:]
        
        # If no such pair is found, just remove the last occurrence of the digit
        return number[:number.rfind(digit)] + number[number.rfind(digit) + 1:]

