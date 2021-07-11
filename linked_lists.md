---
title: CSE 212 Final Project
description: "Lesson 2: Linked Lists"
---

## Introduction

Linked lists are a non-contiguous list of items. This means that its items are not adjacent to another in memory. Linked lists are made up of nodes that contain the data and a reference to the next node in the list. Because items in a linked list do not reside next to each other in memory, they cannot be accessed by index. Instead, you must start at the head (the first item) of the list and traverse each link until you find the desired item.

## Singly and Doubly Linked Lists

A singly linked list only has links going in one direction. Each node has one reference to the next item in the list, meaning that you must always start at the head and end at the tail.

A doubly linked list has two references, both to the previous node and to the following node. This allows you to traverse the list both backwards and forwards, starting at the head or the tail.


## Traversing and Modifying

Here's some **Python** code we can use to print out the values of each item in the linked list. Don't worry, later on we'll take a look at how our linked list class is made!

```py
# Get a reference to the first item in the list.
node = linked_list.head

# Start the loop.
while node is not None:
    # Print out the data contained in the node.
    print(node.data)
    # node.next refers to the next node in the list.
    # We'll assign it to our current node variable to continue traversing the list.
    node = node.next
```


## Efficiency

Let's compare the efficiency of linked lists to a regular dynamic array:

|                   | Dynamic Array | Linked List |
| ----------------- | :-----------: | :---------: |
| Access element    |    `O(1)`     |   `O(n)`    |
| Add/remove middle |    `O(n)`     |   `O(1)`    |
| Add/remove end    |    `O(1)`     |   `O(1)`    |

Both types of lists have their pros and cons. Dynamic arrays give you immediate access to its elements, but it's slower modifying them. Linked lists require you to traverse each element, but you can easily add a new element at any position in the list.


## Application

## Practice

## Problems
### 1.

<textarea>
# Write your code here!
</textarea>

<details><summary markdown="span">See the solution!</summary>

```py

```

</details>


### 2.

<textarea>
# Write your code here!
</textarea>

<details><summary markdown="span">See the solution!</summary>

```py

```

</details>

---

### Keep on learning!

Linked lists can be tricky. Lots of people can't make **head or tail** out of them, so way to go for making it his far!

The next lesson is [Trees](trees.md)!

Or review the last lesson on [Stacks](stacks.md)!

<!-- Primary Color: #0F60D0 -->