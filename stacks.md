---
title: CSE 212 Final Project
description: "Lesson 1: Stacks"
---

<!-- # Lesson 1 - Stack -->

<!-- - [Introduction](#Introduction)
- [Pushing and Popping](#Pushing-and-Popping)
- [The Call Stack](#The-Call-Stack)
- [Efficiency](#Efficiency)
- [Example – Reversing items](#Example-–-Reversing-items)
- [Problem to Solve](#Problem-to-Solve) -->

## Introduction

Stacks are a type of dynamic array that only gives the user access to the top element.


## Pushing and Popping

The functions used for modifying the top element of a stack are called `push` and `pop`.

The `push()` function adds an item to the top of the stack.

```py
stack = []

stack.push(1)
stack.push(2)
stack.push(3)

print(stack)
# [ 1, 2, 3 ]
```

The `pop()` function removes the top item and returns its value.

```py
print(stack.pop())  # 3
print(stack.pop())  # 2
print(stack.pop())  # 1
```


## The Call Stack
## Efficiency
## Example – Reversing items

Because items are popped from the stuck in the opposite order that they are pushed, stacks can be useful for reversing the order of a list.

```py
stack = list("Word")
word_reversed = ""
while len(stack) > 0:
  word_reversed.append(stack.pop())
```

## Problem to Solve



<details><summary>See Solution</summary>

```py
stack = []

stack.push(1)
stack.push(2)
stack.push(3)
three = stack.pop()
two = stack.pop()
one = stack.pop()
print(one, two, three)
```

</details>
