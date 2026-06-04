class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for item in s:
            if len(stack) == 0 and item in "}])":
                return False
            if item in "({[":
                stack.append(item)
            else:
                opener = stack.pop()
                if opener + item in "() [] {}":
                    continue # right
                else:
                    return False
        
        return len(stack) == 0