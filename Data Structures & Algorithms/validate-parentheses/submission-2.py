class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for item in s:
            if item in "({[":
                stack.append(item)
            else:
                if len(stack) == 0:
                    return False
                opener = stack.pop()
                if opener + item in "() [] {}":
                    continue # right
                else:
                    return False
        
        return len(stack) == 0