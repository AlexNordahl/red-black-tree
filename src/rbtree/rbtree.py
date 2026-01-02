from node import Node, NodeColor

class RedBlackTree:
    def __init__(self, key, value = None):
        self.NIL = Node(key=None, color=NodeColor.BLACK)

        self.root = Node(key=key, value=value, color=NodeColor.BLACK)
        self._nilify(self.root)

    def insert(self, key, value = None):
        if self.root is self.NIL:
            self.root = Node(key=key, value=value, color=NodeColor.BLACK)
            self._nilify(self.root)
            return

        node = Node(key=key, value=value, color=NodeColor.RED)
        self._nilify(node)
        
        curr = self.root
        while curr is not self.NIL:
            if node.key < curr.key:
                if curr.left is self.NIL:
                    curr.left = node
                    self._nilify(curr.left)
                    break
                curr = curr.left
            elif node.key > curr.key:
                if curr.right is self.NIL:
                    curr.right = node
                    self._nilify(curr.right)
                    break
                curr = curr.right

    def delete(self, key):
        pass

    def search(self, key):
        pass

    def contains(self, key):
        pass

    def _nilify(self, node):
        if node.left is None: node.left = self.NIL
        if node.right is None: node.right = self.NIL
        if node.parent is None: node.parent = self.NIL