import random
from src.rbtree.rbtree import RedBlackTree
from src.rbtree.node import NodeColor

def _is_nil(t: RedBlackTree, n) -> bool:
    return n is t.NIL

def _nodes_inorder_no_nil(t: RedBlackTree):
    return [n for n in t.inorder(t.root) if n is not t.NIL]

def _assert_bst_property(t: RedBlackTree):
    nodes = _nodes_inorder_no_nil(t)
    keys = [n.key for n in nodes]
    assert keys == sorted(keys)
    assert len(keys) == len(set(keys))

def _assert_nil_is_black(t: RedBlackTree):
    assert t.NIL.color is NodeColor.BLACK

def _assert_root_is_black(t: RedBlackTree):
    assert t.root is not t.NIL
    assert t.root.key is not None
    assert t.root.color is NodeColor.BLACK

def _assert_no_red_red_edges(t: RedBlackTree):
    def dfs(n):
        if _is_nil(t, n):
            return
        if n.color is NodeColor.RED:
            assert n.left.color is NodeColor.BLACK
            assert n.right.color is NodeColor.BLACK
        dfs(n.left)
        dfs(n.right)

    dfs(t.root)

def _black_height(t: RedBlackTree, node) -> int:
    if _is_nil(t, node):
        return 1

    left_bh = _black_height(t, node.left)
    right_bh = _black_height(t, node.right)
    assert left_bh == right_bh, "Black-height mismatch between left and right subtree"

    return left_bh + (1 if node.color is NodeColor.BLACK else 0)

def _assert_black_height_consistent(t: RedBlackTree):
    _black_height(t, t.root)

def _assert_parent_links_consistent(t: RedBlackTree):
    assert t.root.parent is t.NIL

    def dfs(n):
        if _is_nil(t, n):
            return
        if not _is_nil(t, n.left):
            assert n.left.parent is n
        if not _is_nil(t, n.right):
            assert n.right.parent is n
        dfs(n.left)
        dfs(n.right)

    dfs(t.root)

def assert_rb_invariants(t: RedBlackTree):
    _assert_nil_is_black(t)
    _assert_root_is_black(t)
    _assert_bst_property(t)
    _assert_no_red_red_edges(t)
    _assert_black_height_consistent(t)
    _assert_parent_links_consistent(t)

def test_init_sets_root_and_is_black():
    t = RedBlackTree(10)

    assert t.root is not t.NIL
    assert t.root.key == 10
    assert t.root.color is NodeColor.BLACK

    assert_rb_invariants(t)

def test_insert_second_element_keeps_bst_and_rb_properties():
    t = RedBlackTree(10)
    t.insert(5)

    assert [n.key for n in _nodes_inorder_no_nil(t)] == [5, 10]

    assert_rb_invariants(t)

def test_insert_three_triggers_rebalance_cases_eventually():
    t = RedBlackTree(10)
    t.insert(5)
    t.insert(1)

    assert [n.key for n in _nodes_inorder_no_nil(t)] == [1, 5, 10]
    assert_rb_invariants(t)

def test_insert_updates_value_on_duplicate_key():
    t = RedBlackTree(7)
    t.insert(7)

    n = t.search(7)
    assert n is not t.NIL
    assert_rb_invariants(t)

def test_search_missing_returns_nil():
    t = RedBlackTree(2)
    t.insert(1)
    t.insert(3)

    assert t.search(999) is t.NIL
    assert_rb_invariants(t)

def test_many_inserts_increasing_order():
    t = RedBlackTree(1)
    for k in range(2, 51):
        t.insert(k)

    inorder_keys = [n.key for n in _nodes_inorder_no_nil(t)]
    assert inorder_keys == list(range(1, 51))

    assert_rb_invariants(t)

def test_many_inserts_decreasing_order():
    t = RedBlackTree(50)
    for k in range(49, 0, -1):
        t.insert(k)

    inorder_keys = [n.key for n in _nodes_inorder_no_nil(t)]
    assert inorder_keys == list(range(1, 51))
    assert_rb_invariants(t)

def test_random_inserts_match_sorted_unique_keys():
    random.seed(123)

    keys = [random.randint(1, 200) for _ in range(200)]
    unique = sorted(set(keys))

    t = RedBlackTree(keys[0])
    for k in keys[1:]:
        t.insert(k)

    inorder_keys = [n.key for n in _nodes_inorder_no_nil(t)]
    assert inorder_keys == unique

    for k in [unique[0], unique[len(unique)//2], unique[-1]]:
        assert t.search(k) is not t.NIL

    assert_rb_invariants(t)