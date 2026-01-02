from enum import Enum

class NodeColor(Enum):
    RED = 'Red'
    BLACK = 'Black'

class Node:
    def __init__(self, key, value = None, color = NodeColor.RED):
        self.key = key
        self.value = value
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return f"key={self.key} value={self.value} color={self.color.value}"
    
    def __repr__(self):
        return f"Node({self.key!r}, {self.value!r}, {self.color!r}, {self.left!r}, {self.right!r}, {self.parent!r})"
    
    def __eq__(self, other):
        return self.key == other.key and self.value == other.value and self.color == other.color
    
    def __ne__(self, other):
        return not self == other