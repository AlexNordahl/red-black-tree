## Running Program
![Program Example](/examples/running.png)

## Rendered Graph Example
![Program Example](/examples/graph.png)

## Table Of Contents

1. Introduction
2. Project Structure
4. Used Libraries
5. Classes
6. Summary

## 1. Introduction

Project is a classic implementation of a Red-Black Tree (self-balancing binary search tree).
It provides the user with the ability to insert nodes at runtime, search values, and render the current structure of the tree using Graphviz.

## 2. Project Structure

Example project layout:
```
project_root/
│               
└─ src/rbtree
   ├─ __init__.py
   ├─ main.py                  # CLI entry point (interactive commands)
   ├─ node.py                  # Node + NodeColor definitions
   ├─ rbtree.py                # RedBlackTree implementation
   ├─ rbtree_graph.py          # RBTreeGraph (Graphviz rendering)
   └─ prints.py                # print_banner(), print_manual()               
└─ tests
   ├─ __init__.py
   ├─ test_insertion.py
   ├─ test_node.py
   └─ test_rotation.py
```

Main script imports:
- RedBlackTree from rbtree.py
- RBTreeGraph from rbtree_graph.py
- CLI text helpers from prints.py

## 3. Used Libraries
Standard / internal modules

- node.py provides:

    - Node – tree node structure (key, color, left/right/parent)

    - NodeColor – enum-like color values (RED, BLACK)

External library

- graphviz (from graphviz import Graph)
Used for rendering the tree into an image (png by default).
RBTreeGraph builds nodes/edges and calls dot.render().

## 4. Classes

### `Node`

Represents a single node in the red-black tree.

Each node stores:
- `key` – value stored in the node (`None` is used for the NIL sentinel),
- `color` – node color (`RED` or `BLACK`),
- `left` – reference to the left child,
- `right` – reference to the right child,
- `parent` – reference to the parent node.

The `Node` class is used both for regular tree nodes and for the special `NIL` sentinel node, which simplifies tree operations by eliminating `None` checks.

---

### `NodeColor`

Defines possible colors of a red-black tree node.

Available values:
- `RED`
- `BLACK`

This class is used to clearly distinguish node colors and to simplify color comparisons during tree balancing operations.

---

### `RedBlackTree`

Main class implementing the red-black tree data structure.

Key features:
- Uses a single shared `NIL` sentinel node instead of `None`
- Automatically balances the tree after each insertion
- Guarantees logarithmic time complexity for insertion and search

Main attributes:
- `root` – root of the tree
- `NIL` – black sentinel node representing all leaf nodes

Main methods:
- `insert(key)` – inserts a new key into the tree and restores red-black properties
- `search(key)` – searches for a node with the given key
- `inorder(node)` – returns an inorder traversal of the tree
- `clear()` – removes all nodes from the tree

Internal helper methods:
- `_left_rotate(node)` – performs a left rotation
- `_right_rotate(node)` – performs a right rotation
- `_insert_fixup(node)` – restores red-black properties after insertion
- `_nilify(node)` – replaces `None` references with the `NIL` sentinel

---

### `RBTreeGraph`

Handles visualization of the red-black tree using Graphviz.

Responsibilities:
- Converts the tree structure into a Graphviz graph
- Assigns colors to nodes based on their red-black state
- Renders the tree into an image file

Main methods:
- `supply(tree)` – reads the tree structure and builds a graph representation
- `render()` – generates and displays the rendered tree
- `clear()` – resets the internal Graphviz graph

## 5. Summary

This project presents a complete implementation of a red-black tree with an interactive command-line interface and graphical visualization support.

The application allows users to dynamically insert and search for values while ensuring that all red-black tree properties are preserved through rotations and recoloring. Thanks to the use of a NIL sentinel node, the implementation avoids special-case handling of null pointers and keeps the code clean and consistent.

Additionally, the integration with Graphviz enables clear visualization of the tree structure, making the project useful not only as a data structure implementation but also as an educational tool for understanding how red-black trees maintain balance.