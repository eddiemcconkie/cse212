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
        ...

    def add_after(self, value, data):
        for node in self:
            if node.data == value:
                if node == self.tail:
                    # If our target value is at the tail, call the regular add_at_tail function.
                    self.add_at_tail(data)
                else:
                    # Create the new node.
                    new_node = LinkedList.Node(data)
                    # Connect the new node to the node on the right (node.next).
                    new_node.next = node.next
                    node.next.prev = new_node
                    # Connect the new node to the node on the left (node).
                    node.next = new_node
                    new_node.prev = node

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

print(linkedlist)
# Should print: [7 -> 9 -> 6 -> 4 -> 8 -> 5]

# Using the __reversed__ method.
print("Reversed:")
for node in reversed(linkedlist):
    print(node.data)
