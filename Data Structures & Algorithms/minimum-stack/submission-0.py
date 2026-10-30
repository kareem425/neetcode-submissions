class MinStack:

    def __init__(self):
        self.stack = []
        self.minst = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.minst:
            self.minst.append(val)
        elif val < self.minst[-1]:
            self.minst.append(val)
        else:
            self.minst.append(self.minst[-1])

    def pop(self) -> None:
        self.stack.pop()

        self.minst.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minst[-1]