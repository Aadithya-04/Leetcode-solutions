class Solution:
    def myAtoi(self, s: str) -> int:
        int_min = -2**31
        int_max = 2**31-1

        # Step 1: Remove leading whitespace
        s = s.lstrip()
        if not s:
            return 0
        
        # Step 2: Check the sign
        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        
        # Step 3: Read the number
        num = 0
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            else:
                break
        
        # Apply the sign
        num *= sign
        
        # Step 4: Clamp the number within the 32-bit range
        if num < int_min:
            return int_min
        if num > int_max:
            return int_max
        
        return num