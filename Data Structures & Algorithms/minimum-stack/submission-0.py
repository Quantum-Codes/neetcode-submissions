class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        minimum = val
        if self.stack:
            if val > self.stack[-1][1]:
                minimum = self.stack[-1][1]

        self.stack.append((val, minimum))
            
    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
        
