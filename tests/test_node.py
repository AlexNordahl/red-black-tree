import pytest
from src.rbtree.node import Node, NodeColor

@pytest.fixture
def empty_node():
    node = Node(10, NodeColor.BLACK)
    return node

@pytest.fixture
def not_empty_node():
    node = Node(4, NodeColor.BLACK, Node(2, NodeColor.RED), Node(6, NodeColor.RED))
    return node

def test_str(empty_node, not_empty_node):
    assert str(empty_node) == "10(Black)"
    assert str(not_empty_node) == "4(Black)"

def test_repr(empty_node, not_empty_node):
    assert repr(empty_node) == "Node(10, <NodeColor.BLACK: 'Black'>, None, None)"
    assert repr(not_empty_node) == "Node(4, <NodeColor.BLACK: 'Black'>, Node(2, <NodeColor.RED: 'Red'>, None, None), Node(6, <NodeColor.RED: 'Red'>, None, None))"

def test_eq(empty_node):
    assert not empty_node == Node(15, NodeColor.RED)
    assert empty_node == Node(10, NodeColor.BLACK)

def test_ne(empty_node, not_empty_node):
    assert not empty_node != empty_node
    assert empty_node != not_empty_node