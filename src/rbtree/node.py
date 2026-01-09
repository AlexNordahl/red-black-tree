from enum import Enum

class NodeColor(Enum):
    RED = 'Red'
    BLACK = 'Black'

class Node:
    def __init__(self, key, color = NodeColor.RED):
        self.key = key
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return f"key={self.key} color={self.color.value}"
    
    def __repr__(self):
        return f"Node({self.key!r}, {self.color!r})"
    
    def __eq__(self, other):
        return self.key == other.key and self.color == other.color
    
    def __ne__(self, other):
        return not self == other