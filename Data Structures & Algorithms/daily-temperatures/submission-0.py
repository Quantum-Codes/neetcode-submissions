class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        out = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            if not stack:
                stack.append(i)
                continue
                # there was nothing to track. so i pushed something

            # keeps popping solved ones.
            while stack and temperatures[i] > temperatures[stack[-1]]:
                initial = stack.pop()
                out[initial] = i - initial
            
            stack.append(i)
            
        return out