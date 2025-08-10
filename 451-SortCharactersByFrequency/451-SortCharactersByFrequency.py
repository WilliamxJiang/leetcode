# Last updated: 8/10/2025, 3:06:34 PM
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #for each day i, look forward to find the first warmer temperature, and then just find diff in days
        """
        for i in range (len(temps))
            for j in range(i+1)
                if temps[j[ > temps]]

        n = len(temperatures)
        answer = [0] * n
        for i in range(n):
            for j in range(i + 1, n):
                if temperatures[j] > temperatures[i]:
                    answer[i] = j - i
                    break
        return answer"""
        #create a stack, iterate over each day, if stack is not empty and the temp > then top of stack
        n = len(temperatures)
        answer = [0] * n
        stack = []

        for i, temp in enumerate(temperatures):
            #while stack is not empty and current temp > than top stack
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                answer[prev_index] = i - prev_index
            stack.append(i)
        return answer