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

def test_LL_imbalance():
    rbt = RedBlackTree(10)
    rbt.insert(8)
    rbt.insert(6)

    node10 = rbt.search(10)
    node8 = rbt.search(8)
    node6 = rbt.search(6)

    rbt._right_rotate(node10)

    assert node8.right is node10
    assert node8.left is node6
    assert node6.parent is node8
    assert node10.parent is node8

def test_LR_imbalance():
    rbt = RedBlackTree(10)
    rbt.insert(8)
    rbt.insert(9)

    node10 = rbt.search(10)
    node8 = rbt.search(8)
    node9 = rbt.search(9)

    rbt._left_rotate(node8)
    rbt._right_rotate(node10)

    assert node9.left is node8
    assert node9.right is node10
    assert node8.parent is node9
    assert node10.parent is node9

def test_RL_imbalance():
    rbt = RedBlackTree(10)
    rbt.insert(20)
    rbt.insert(15)

    node10 = rbt.search(10)
    node15 = rbt.search(15)
    node20 = rbt.search(20)

    rbt._right_rotate(node20)
    rbt._left_rotate(node10)

    assert node15.left is node10
    assert node15.right is node20
    assert node10.parent is node15
    assert node20.parent is node15