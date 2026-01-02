from enum import Enum

class NodeColor(Enum):
    RED = 'Red'
    BLACK = 'Black'

class Node:
    def __init__(self, data, color, left = None, right = None):
        self.data = data
        self.color = color
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.data}({self.color.value})"
    
    def __repr__(self):
        return f"Node({self.data!r}, {self.color!r}, {self.left!r}, {self.right!r})"
    
    def __eq__(self, other):
        return self.data == other.data and self.color == other.color
    
    def __ne__(self, other):
        return not self == other