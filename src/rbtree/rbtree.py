from .node import Node, NodeColor

class RedBlackTree:
    def __init__(self, key = None):
        self.NIL = Node(key=None, color=NodeColor.BLACK)

        if key is not None:
            self.root = Node(key=key, color=NodeColor.BLACK)
            self._nilify(self.root)
        else:
            self.root = self.NIL

    def insert(self, key):
        node = self.NIL
        if self.root is self.NIL:
            node = Node(key=key, color=NodeColor.BLACK)
            self.root = node
        else:
            node = Node(key=key, color=NodeColor.RED)

        self._nilify(node)

        y = self.NIL
        curr = self.root

        while curr is not self.NIL:
            y = curr
            if node.key < curr.key:
                curr = curr.left
            elif node.key > curr.key:
                curr = curr.right
            else:
                return

        node.parent = y
        if y is self.NIL:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

        self._insert_fixup(node)

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
    
    def clear(self):
        self.root = self.NIL

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

    def _insert_fixup(self, node):
        while node.parent.color is NodeColor.RED:
            if node.parent is node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color is NodeColor.RED:
                    node.parent.color = NodeColor.BLACK
                    uncle.color = NodeColor.BLACK
                    node.parent.parent.color = NodeColor.RED
                    node = node.parent.parent
                else:
                    if node is node.parent.right:
                        node = node.parent
                        self._left_rotate(node)
                    node.parent.color = NodeColor.BLACK
                    node.parent.parent.color = NodeColor.RED
                    self._right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color is NodeColor.RED:
                    node.parent.color = NodeColor.BLACK
                    uncle.color = NodeColor.BLACK
                    node.parent.parent.color = NodeColor.RED
                    node = node.parent.parent
                else:
                    if node is node.parent.left:
                        node = node.parent
                        self._right_rotate(node)
                    node.parent.color = NodeColor.BLACK
                    node.parent.parent.color = NodeColor.RED
                    self._left_rotate(node.parent.parent)

        self.root.color = NodeColor.BLACK
        self.root.parent = self.NIL

    def _nilify(self, node):
        if node.left is None: node.left = self.NIL
        if node.right is None: node.right = self.NIL
        if node.parent is None: node.parent = self.NIL

    def _root(self):
        return self.root
    
    def _NIL(self):
        return self.NIL