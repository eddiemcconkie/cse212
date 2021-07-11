### Practice

stack = []

stack.append(1)  # [1]
stack.append(2)  # [1, 2]
stack.append(3)  # [1, 2, 3]
stack.pop()      # [1, 2]
stack.pop()      # [...]
stack.append(4)  # [...]
stack.append(5)  # [...]
stack.pop()      # [...]
stack.append(6)  # [...]
stack.pop()      # [...]
stack.pop()      # [...]
stack.pop()      # [...]
stack.append(7)  # [...]
stack.append(8)  # [...]
stack.pop()      # [...]
stack.append(9)  # [...]
stack.append(10) # [...]
stack.pop()      # [...]


### Problem 1

phrase = "!looc era serutcurts ataD"
phrase_reversed = ""
stack = []

for letter in phrase:
    stack.append(letter)

while len(stack) > 0:
    last_letter = stack.pop()
    phrase_reversed.append(last_letter)

print(phrase_reversed)
# "Data structures are cool!"


### Problem 2

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

    # Here are some extra functions we can add to our Stack Class!
    def __len__(self):
        return len(self.stack)

    def __str__(self):
        return str(self.stack)

    def clear(self):
        self.stack = []