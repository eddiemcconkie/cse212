import random


class LinkedList:

    # The linked list has a node as an inner class.
    class Node:
        def __init__(self, data):
            # Initialize the data for the node.
            self.data = data
            # The node starts off without any connections.
            self.next = None
            self.prev = None

        def set_data(self, data):
            self.data = data

    def __init__(self):
        # The linked list starts out without a head or tail.
        self.head = None
        self.tail = None

    def add_at_head(self, data):
        # Create the new node.
        node = LinkedList.Node(data)

        if self.head:
            # 1. Connect the new node to the old head node.
            node.next = self.head
            # 2. Connect the old head node back to the new node to doubly link it.
            self.head.prev = node
            # 3. Point the head reference to the new node.
            self.head = node
        else:
            # If the linked list has no head, it has no tail either. Set both to the new node.
            self.head = node
            self.tail = node

    def add_at_tail(self, data):
        # (The add_at_head function should help).
        node = LinkedList.Node(data)

        if self.tail:
            # 1. Connect the new node to the old head node.
            node.prev = self.tail
            # 2. Connect the old head node back to the new node to doubly link it.
            self.tail.next = node
            # 3. Point the head reference to the new node.
            self.tail = node
        else:
            # If the linked list has no head, it has no tail either. Set both to the new node.
            self.head = node
            self.tail = node

    def add_after(self, value, data):
        for curr in self:
            if curr.data == value:
                if curr == self.tail:
                    # If our target value is at the tail, call the regular add_at_tail function.
                    self.add_at_tail(data)
                else:
                    # Create the new node.
                    new = LinkedList.Node(data)
                    # Connect the new node to the node on the right (node.next).
                    new.next = curr.next
                    curr.next.prev = new
                    # Connect the new node to the node on the left (node).
                    curr.next = new
                    new.prev = curr

                # We only want to insert after the first value.
                break

    def add_before(self, value, data):
        # (The add_after function should help).
        ...

    def remove_head(self):
        self.head = self.head.next
        self.head.prev = None

    def remove_tail(self):
        self.tail = self.tail.prev
        self.tail.next = None

    def remove(self, value):
        # Remove the first occurrence of a value.
        ...

    def replace(self, value, data):
        # You may want to make use of the set_data function within the Node class.
        ...

    def __iter__(self):
        # Iterate through the linked list.
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __reversed__(self):
        # Allows you to iterate through the list backward.
        node = self.tail
        while node is not None:
            yield node
            node = node.prev

    def __str__(self):
        # Returns a string representation of the list.
        data = [str(node.data) for node in self]
        return f"[{' -> '.join(data)}]"

    def add_sorted(self, data):
        # If the list is empty, initialize the list with the node.
        if self.head is None:
            new = LinkedList.Node(data)
            self.head = new
            self.tail = new
            return

        # Iterate over the nodes in the list to find the correct position.
        for curr in self:
            # If the data is less than the head, add at the head.
            if curr == self.head and data <= self.head.data:
                self.add_at_head(data)
                return
            # If the data is greater than the tail, add at the tail.
            elif curr == self.tail:
                self.add_at_tail(data)
                return
            # Find a position for the data in the list.
            else:
                if curr.data <= data < curr.next.data:
                    new = LinkedList.Node(data)
                    new.next = curr.next
                    curr.next.prev = new
                    curr.next = new
                    new.prev = curr
                    return


linkedlist = LinkedList()
linkedlist.add_at_head(1)
linkedlist.add_at_head(2)
linkedlist.add_at_head(3)
linkedlist.add_after(2, 6)
linkedlist.add_after(3, 7)
linkedlist.remove_head()
# Uncomment the tests below after you have implemented the functions.
# linkedlist.add_at_tail(4)
# linkedlist.add_at_tail(5)
# linkedlist.add_before(5, 8)
# linkedlist.replace(2, 9)
# linkedlist.remove(1)

# print(linkedlist)
# Should print: [7 -> 9 -> 6 -> 4 -> 8 -> 5]

# Using the __reversed__ method.
# print("Reversed:")
# for node in reversed(linkedlist):
#     print(node.data)


linkedlist_sorted = LinkedList()

for i in range(100):
    number = random.randint(0, 100)
    linkedlist_sorted.add_sorted(number)

print(linkedlist_sorted)
