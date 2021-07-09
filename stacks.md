---
title: CSE 212 Final Project
description: "Lesson 1: Stacks"
---

## Introduction

Stacks are a type of dynamic array that only gives the user access to the top element. They are Last In First Out (LIFO)


## Pushing and Popping

The functions used for modifying the top element of a stack are called `push` and `pop`.

![push and pop](img/stack01.drawio.png)

Python uses the `append()` function for pushing an item to the top of the stack.

```py
stack = []

stack.append(1)
stack.append(2)
stack.append(3)

print(stack)
# [ 1, 2, 3 ]
```

The `pop()` function removes the top item and returns its value, allowing you to store the popped value in another variable. In the example below, the values popped from the stack are returned to the `print()` function and displayed.

```py
print(stack.pop())  # 3
print(stack.pop())  # 2
print(stack.pop())  # 1
```


## Efficiency

Pushing and popping from the stack doesn't require any shifting of the data in the dynamic array. The top item is only ever accessed, which means modifying the stack has an efficiency of `O(1)`. 


## Application – Keeping things in order

Stacks are really good at keeping things in order. For example, when you're writing code in your code editor and you make a mistake, you can hit Ctrl Z to undo, and that's because all of your changes are saved on a stack. The editor knows the order of all the actions you performed, so undo-ing an action simply means removing it from the stack.

Another good example of how stacks are used is the CallStack. The CallStack keeps track of the state of the program as functions are called, meaning that the values of the variables within that function's scope are saved. Take a look at the diagram below, which shows a structure chart for a program. If you want to call `Function F`, you first have to call `Function B` and `Function D`.

![push and pop](img/stack02.drawio.png)

As each function is called, it is added to the CallStack. When a function finishes or returns a value, it pops the top function off the CallStack and reverts to the previous program state. The CallStack comes especially in handy when debugging. If an error occurs in one of your functions, the CallStack can tell you which functions were called to reach that point, making it much easier to track the source of the error.


## Examples

```py
stack = []

stack.append(1)
stack.append(2)
stack.append(3)
three = stack.pop()
two = stack.pop()
one = stack.pop()
print(three, two, one)
```


## Problem – Reversing items

Time to try stacks out for yourself!

Because items are popped from the stack in the opposite order that they are pushed, stacks can be useful for reversing the order of an array. Finish the Python code below to reverse the phrase

<textarea>
# Write your code here!
phrase = "!looc era serutcurts ataD"
phrase_reversed = ""
stack = []
</textarea>

<details><summary markdown="span">See the solution!</summary>

```py
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
```

</details>


## Problem – Creating a Stack Class

Using Python's list works pretty well, but it's still possible to access items in the middle of the list. Let's practice encapsulating our stack in a class! Try implementing:
- The `push` and `pop` methods
- A `peek` method, which will return the top item without removing it
- An `is_empty` method, which will return a boolean indicating whether the stack is empty
- Any other methods you think would be useful!

<textarea>
# Write your code here!
class Stack:

    def __init__(self):
        self.stack = []

    def push(self, value):
        ...

    def pop(self):
        ...

    def peek(self):
        ...

    def is_empty(self):
        ...
</textarea>

<details><summary markdown="span">See the solution!</summary>

```py
class Stack:
    
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
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
```

</details>

<!-- Primary Color: #0F80D0 -->