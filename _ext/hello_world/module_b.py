from docutils import nodes

from sphinx.application import Sphinx

__all__ = [
    "register",
]


def visit_node(_self: nodes.GenericNodeVisitor, _node: nodes.Node) -> None:
    pass

def depart_node(_self: nodes.GenericNodeVisitor, _node: nodes.Node) -> None:
    pass

class NodeB(nodes.General, nodes.Element):
    pass


def register(app: Sphinx) -> None:
    app.add_node(
        NodeB,
        html=(visit_node, depart_node),
        latex=(visit_node, depart_node),
        text=(visit_node, depart_node),
    )
