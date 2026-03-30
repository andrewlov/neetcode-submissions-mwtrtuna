class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = []
        for i, val in enumerate(temperatures):
            while stack and val > stack[-1][0]:
                stackTemp, stackIndex = stack.pop()
                output[stackIndex] = (i - stackIndex)
            stack.append([val, i])
        return output