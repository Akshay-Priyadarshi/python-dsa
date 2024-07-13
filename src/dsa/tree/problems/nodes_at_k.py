from typing import Optional

from src.helpers.custom_typevars import ComparableType
from tree.implementation import TreeNode


def print_nodes_at_k(node: Optional[TreeNode[ComparableType]], k: int) -> None:
    if node is None:
        return
    if k == 0:
        print(node.data)
    else:
        print_nodes_at_k(node.left, k - 1)
        print_nodes_at_k(node.right, k - 1)
