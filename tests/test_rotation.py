import pytest
from src.rbtree.node import Node, NodeColor
from src.rbtree.rbtree import RedBlackTree

def test_single_node():
    rbt = RedBlackTree(10)
    with pytest.raises(Exception):
        rbt._left_rotate(rbt.search(10))

def test_RR_imbalance():
    rbt = RedBlackTree(10)
    rbt.insert(15)
    rbt.insert(20)

    node10 = rbt.search(10)
    node15 = rbt.search(15)
    node20 = rbt.search(20)

    rbt._left_rotate(node10)

    assert node15.right is node20
    assert node15.left is node10
    assert node10.parent is node15
    assert node20.parent is node15