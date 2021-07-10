class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(str(element))

    def pop(self):
        if self.data:
            return self.data.pop()

    def top(self):
        if self.data:
            return self.data[-1]

    def is_empty(self):
        if not self.data:
            return True
        return False

    def __str__(self):
        return "[" + ", ".join(reversed(self.data)) + "]"


stack = Stack()
stack.push(5)
stack.push(4)
stack.push(3)
stack.push(2)
stack.push(1)
print(stack.pop())
print(stack.top())
print(stack.is_empty())
print(stack)
