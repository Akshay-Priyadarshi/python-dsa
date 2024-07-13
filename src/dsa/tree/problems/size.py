from typing import Optional
from tree.implementation import TreeNode
from src.helpers.custom_typevars import ComparableType


def get_size(node: Optional[TreeNode[ComparableType]]) -> int:
    if node is None:
        return 0
    return get_size(node.left) + get_size(node.right) + 1
