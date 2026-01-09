import pytest
from src.rbtree.node import Node, NodeColor

@pytest.fixture
def empty_node():
    node = Node(key=1, color=NodeColor.BLACK)
    return node

@pytest.fixture
def not_empty_node():
    node = Node(key=4, color=NodeColor.BLACK)
    node.left = Node(key=2, color=NodeColor.RED)
    node.right = Node(key=6, color=NodeColor.RED)
    return node

def test_str(empty_node, not_empty_node):
    assert str(empty_node) == "key=1 color=Black"
    assert str(not_empty_node) == "key=4 color=Black"

def test_repr(empty_node, not_empty_node):
    assert repr(empty_node) == "Node(1, <NodeColor.BLACK: 'Black'>)"
    assert repr(not_empty_node) == "Node(4, <NodeColor.BLACK: 'Black'>)"

def test_eq(empty_node):
    assert empty_node == empty_node
    assert empty_node == Node(key=1, color=NodeColor.BLACK)

def test_ne(empty_node, not_empty_node):
    assert empty_node != not_empty_node
    assert not empty_node != empty_node