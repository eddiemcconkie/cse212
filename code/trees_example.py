class BST:

    def __init__(self):
        self.root = None

    class Node:

        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def add(self, data):
        if self.root:
            self._add_recursive(self.root, data)
        else:
            self.root = BST.Node(data)

    def _add_recursive(self, node, data):
        if data < node.data:
            if node.left:
                self._add_recursive(node.left, data)
            else:
                node.left = BST.Node(data)

        elif data > node.data:
            if node.right:
                self._add_recursive(node.right, data)
            else:
                node.right = BST.Node(data)

    def find(self, data):
        return self._find_recursive(self.root, data)

    def _find_recursive(self, node, data):
        if node is None:
            return False

        if data == node.data:
            return True

        if data < node.data:
            return self._find_recursive(node.left, data)

        if data > node.data:
            return self._find_recursive(node.right, data)

    def _display_recursive(self, node):
        if node:
            self._display_recursive(node.left)
            print(node.data)
            self._display_recursive(node.right)

    def __str__(self):
        self._display_recursive(self.root)
        return ''


bst = BST()
bst.add(4)
bst.add(2)
bst.add(6)
bst.add(1)
bst.add(3)
bst.add(5)
bst.add(7)
print(bst.find(3))  # Should print True
print(bst.find(0))  # Should print False
print(bst.find(6))  # Should print True
print(bst.find(8))  # Should print False
