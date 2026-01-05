from .node import Node, NodeColor

class RedBlackTree:
    def __init__(self, key = None, value = None):
        self.NIL = Node(key=None, color=NodeColor.BLACK)

        self.root = Node(key=key, value=value, color=NodeColor.BLACK)
        self._nilify(self.root)

    def insert(self, key, value = None):
        node = Node(key=key, value=value, color=NodeColor.RED)
        self._nilify(node)
        
        curr = self.root
        while curr is not self.NIL:
            if node.key < curr.key:
                if curr.left is self.NIL:
                    curr.left = node
                    node.parent = curr
                    self._nilify(curr.left)
                    break
                curr = curr.left
            elif node.key > curr.key:
                if curr.right is self.NIL:
                    curr.right = node
                    node.parent = curr
                    self._nilify(curr.right)
                    break
                curr = curr.right

    def inorder(self, node):
        res = []
        if node:
            res = self.inorder(node.left)
            res.append(node)
            res = res + self.inorder(node.right)
        return res

    def search(self, key):
        curr = self.root
        while curr is not self.NIL and key is not curr.key:
            if key < curr.key:
                curr = curr.left
            elif key > curr.key:
                curr = curr.right
            
        return curr

    def _left_rotate(self, node):
        if node.right is self.NIL:
            raise ValueError("cannot left rotate if node.right is NIL")

        v = node.right
        node.right = v.left

        if v.left is not self.NIL:
            v.left.parent = node

        v.parent = node.parent
        if node.parent is self.NIL:
            self.root = v
        elif node.parent.left is node:
            node.parent.left = v
        else:
            node.parent.right = v
        
        v.left, node.parent = node, v

    def _right_rotate(self, node):
        if node.left is self.NIL:
            raise ValueError("cannot right rotate if node.left is NIL")
        
        v = node.left
        node.left = v.right

        if v.right is not self.NIL:
            v.right.parent = node

        v.parent = node.parent
        if node.parent is self.NIL:
            self.root = v
        elif node.parent.right is node:
            node.parent.right = v
        else:
            node.parent.left = v
        
        v.right, node.parent = node, v

    def _nilify(self, node):
        if node.left is None: node.left = self.NIL
        if node.right is None: node.right = self.NIL
        if node.parent is None: node.parent = self.NIL