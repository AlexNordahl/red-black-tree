from .rbtree import RedBlackTree
from .node import NodeColor
from graphviz import Graph

class RBTreeGraph:
    def __init__(self, format="png"):
        self.dot = Graph(format=format)
        self._set_graph_style()
        self._set_node_style()

    def supply(self, graph: RedBlackTree):
        nodes = graph.inorder(graph._root())
        for node in nodes:
            fillcolor = "red" if node.color is NodeColor.RED else "black"
            if node is not graph._NIL():
                self.dot.node(name=str(node.key), label=str(node.key), fillcolor=fillcolor)

            if node.left and node.left is not graph._NIL():
                self.dot.edge(str(node.key), str(node.left.key))

            if node.right and node.right is not graph._NIL():
                self.dot.edge(str(node.key), str(node.right.key))

    def clear(self):
        self.dot.clear()
        self.__init__()

    def render(self, fname="tmp_graph", view=True, cleanup=True):
        self.dot.render(filename=fname, view=view, cleanup=cleanup)

    def _set_graph_style(self):
        self.dot.attr(bgcolor="#3F3F3F", size="10,6", dpi="200")

    def _set_node_style(self):
        self.dot.attr(
            "node",
            shape="circle",
            style="filled",
            fixedsize="true",
            fontname="Helvetica",
            fontcolor="white",
            fontsize="18"
        )
