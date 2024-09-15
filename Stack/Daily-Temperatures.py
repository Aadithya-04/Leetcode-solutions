class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)

        answer = [0]*n #resultant array
        stack = [] # store indices of the array

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]: # condition to check if the current temperature is warmer than the day at the stacks top
                prev_day = stack.pop() #index of the previous day
                answer[prev_day] = i-prev_day
            stack.append(i)

        return answer