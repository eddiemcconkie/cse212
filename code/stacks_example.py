# Stacks Example

class Stack:
    
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def __len__(self):
        return len(self.stack)

    def __str__(self):
        return str(self.stack)
        
        
stack = Stack()
stack.push(5)
stack.push(4)
stack.push(3)
print(stack.pop())
print(len(stack))
print(stack.is_empty())
print(stack.peek())
print(stack)
print(stack.pop())
print(stack.pop())
print(stack.pop())
